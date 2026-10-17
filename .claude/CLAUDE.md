# CLAUDE.md｜vocabuddy-group-9 專案指示檔

## 這是什麼專案
- VocaBuddy：YTP 第 9 組（耶耶耶gobackgoback）的英文單字學習工具，用 Python 寫在 `VocaBuddy.ipynb`，在 Google Colab 執行。
- notebook 只有兩個 cell：cell 0 是資料與核心函式（`vocabulary`、`all_words`、`show_summary`、`run_quiz`、`add_word`）；cell 1 用 `IPython.display` 輸出 HTML/CSS/JS 介面（單字卡、測驗、分類）。
- 單字資料是 cell 0 的 `vocabulary`，格式 `{分類: {英文: 中文}}`；cell 1 從它產生 `words_for_ui`，所以只要改 cell 0，介面會跟著變。
- 組員各用各的 AI 工具：Claude Code 的設定在 `.claude/`，GitHub Copilot 的在 `.github/`；改其中一邊不用動另一邊。
- `check_words.py` 不執行 notebook，用 ast 讀出 `vocabulary` 檢查格式；`labs/` 放 YTP Lab 11～14 的驗收紀錄。

## 怎麼跑起來
- 檢查單字：`python3 check_words.py`，結束碼 0 才算通過；新增或修改單字後一定要跑。
- 測函式（本機沒有 IPython 也能跑）：把 cell 0 的原始碼 `exec` 進一個 dict，用 `answer_provider=lambda q: "…"` 代替 `input` 測 `run_quiz`。
- 介面要在 Colab 或 Jupyter 跑 cell 1 才看得到；本機需要 `pip install ipython`。

## 程式碼慣例（從現有程式碼觀察）
- Python 4 空格縮排；字串用雙引號；函式與變數用 snake_case；輸出用 f-string。
- 每個新函式都要有繁體中文 docstring，第一行固定寫成 `"""用途：…"""`。
- 英文單字一律小寫、去頭尾空白（照 `add_word` 的做法）；同一個英文不可出現在兩個分類。
- 只用 Python 標準函式庫與 `IPython.display`，不加其他套件。
- cell 1 的 JS：DOM 一律用 `$("id")` 取得；顯示使用者輸入用 `textContent`，不要用 `innerHTML`。
- 改 notebook 用 json 讀寫：`json.dumps(nb, indent=2, ensure_ascii=False) + "\n"`，只改 `source`，不動 metadata、輸出與 cell id，保持 diff 最小。

## 協作規矩
- 先說計畫（改哪些檔、為什麼、怎麼驗證），組員回覆同意後才動手。
- 分支 `feature/<短名>`、`fix/<短名>`、`docs/<短名>`；`main` 只透過 PR 合併。
- commit 訊息 `<類型>: <說明>`，類型用 feat／fix／docs／test／refactor／chore，說明可用中文或英文。
- 改完自己驗：跑 `check_words.py`、`git status`、`git diff`，貼出實際輸出；沒跑過的不可寫「通過」。
- 每個 Lab 的驗收證據寫在 `labs/labNN-*/CHECKLIST.md`。

## 不要做的事
- AI 不可自行 commit、merge、push 或開 PR；這些都由組員看過 diff 後決定。
- 不要把 API key 或任何祕密寫進 notebook、文件或 commit。
- 不要改 `vocabulary` 的資料格式，也不要改既有函式的參數（`run_quiz(question_count, answer_provider, category)`、`add_word(english, chinese, category)`）。
- 不要為了讓檢查通過而放寬或刪掉 `check_words.py` 的規則。
- 不要讀或抄導師範例 repo（`vocabuddy-group-mentor`）的成果，所有內容要是本組自己的。
