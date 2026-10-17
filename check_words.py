"""PLAN：檢查 VocaBuddy.ipynb 第一個 cell 的 vocabulary 單字資料。

1. 用 ast 從 notebook 第一個 cell 找出 `vocabulary = {...}`，用 literal_eval 取值（不執行 notebook）。
2. 檢查格式：{分類: {英文: 中文}}，分類與中文不可空白。
3. 檢查英文：小寫、只含英文字母／空格／連字號，且不可重複（同分類內的重複 key 從 ast 抓，literal_eval 會吞掉）。
4. 檢查中文：至少含一個中文字。
5. 全部通過印出總數並以結束碼 0 離開；有錯列出每一條並以結束碼 1 離開。

用法：python3 check_words.py
"""
import ast
import json
import re
import sys
from pathlib import Path

NOTEBOOK = Path(__file__).with_name("VocaBuddy.ipynb")
ENGLISH_PATTERN = re.compile(r"^[a-z]+(?:[ -][a-z]+)*$")
CHINESE_PATTERN = re.compile(r"[\u4e00-\u9fff]")


def load_vocabulary_node(notebook_path):
    """用途：從 notebook 第一個 cell 找出 vocabulary 的 ast 節點，不執行任何程式。"""
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    source = "".join(notebook["cells"][0]["source"])
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "vocabulary" for target in node.targets
        ):
            return node.value
    raise ValueError("第一個 cell 找不到 vocabulary = {...}")


def duplicate_key_errors(vocabulary_node):
    """用途：檢查字典字面值裡重複的 key（literal_eval 會讓後面的值靜默覆蓋前面的）。"""
    errors = []
    if not isinstance(vocabulary_node, ast.Dict):
        return errors
    category_keys = [ast.literal_eval(key) for key in vocabulary_node.keys if key is not None]
    for category in sorted({key for key in category_keys if category_keys.count(key) > 1}):
        errors.append(f"分類重複：{category}")
    for category_key, words_node in zip(vocabulary_node.keys, vocabulary_node.values):
        if category_key is None or not isinstance(words_node, ast.Dict):
            continue
        category = ast.literal_eval(category_key)
        english_keys = [ast.literal_eval(key) for key in words_node.keys if key is not None]
        for english in sorted({key for key in english_keys if english_keys.count(key) > 1}):
            errors.append(f"[{category}] 同分類內英文重複：{english}")
    return errors


def check_vocabulary(vocabulary):
    """用途：檢查單字資料，回傳錯誤訊息清單（空清單代表全部通過）。"""
    errors = []
    seen = {}
    if not isinstance(vocabulary, dict):
        return ["vocabulary 必須是 {分類: {英文: 中文}} 的字典"]
    for category, words in vocabulary.items():
        if not isinstance(category, str) or not category.strip():
            errors.append(f"分類名稱不可空白：{category!r}")
        if not isinstance(words, dict) or not words:
            errors.append(f"分類「{category}」必須是非空的 {{英文: 中文}} 字典")
            continue
        for english, chinese in words.items():
            if not isinstance(english, str) or not ENGLISH_PATTERN.match(english):
                errors.append(f"[{category}] 英文需為小寫英文字母：{english!r}")
            if not isinstance(chinese, str) or not CHINESE_PATTERN.search(chinese):
                errors.append(f"[{category}] {english} 的中文需含中文字：{chinese!r}")
            if english in seen:
                errors.append(f"英文重複：{english}（「{seen[english]}」與「{category}」）")
            else:
                seen[english] = category
    return errors


def main():
    """用途：執行檢查並以結束碼回報結果。"""
    vocabulary_node = load_vocabulary_node(NOTEBOOK)
    vocabulary = ast.literal_eval(vocabulary_node)
    errors = duplicate_key_errors(vocabulary_node) + check_vocabulary(vocabulary)
    if errors:
        for error in errors:
            print(f"✗ {error}")
        sys.exit(1)
    total = sum(len(words) for words in vocabulary.values())
    print(f"vocabulary 檢查通過，共 {len(vocabulary)} 個分類、{total} 個單字 ✓")


if __name__ == "__main__":
    main()
