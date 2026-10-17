# Lab 11 驗收紀錄：開工準備

驗證日期：2026-10-17｜參考：`ytp26h2-labs/labs/lab11-agentic-setup`，改成本組的 Python notebook 版本。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 工具裝好了，終端機回得出版本號 | ✅ | 本機（Fedora）`claude --version` → `2.1.285 (Claude Code)`；`python3 --version` → `Python 3.14.3`。 |
| 2 | 已登入或已設好金鑰，不再跳未認證 | ✅ | Claude Code 以組員帳號登入，沒有未認證提示。本專案不呼叫 API，不需要 API key。 |
| 3 | 在專案資料夾裡啟動，第 3 題答對了 | ✅ | 工作目錄 `~/vocabuddy-group-9`；三題答案見下方。 |
| 4 | 知道自己現在在哪一種操作模式 | ⏳ | 本次 session 是 `auto` 模式（自動接受），不是教材要求的逐步確認；改以「AI 不 commit，組員看過 diff 再決定」補償。要完全符合教材，請組員用 `Shift+Tab` 切到 default（每步詢問）再做一次小改動。 |
| 5 | 完成一次小改動，且自己用 git diff 驗過才提交 | ⏳ | 改動：`VocaBuddy.ipynb` cell 0 新增分類「程式」：loop→迴圈、variable→變數、debug→除錯（`VocaBuddy.ipynb:25`～`29`）。AI 已驗證（見下）；**待組員看過 `git diff` 後自己 commit**（目前 notebook 的 diff 也含 Lab 12 的 `shuffle_words()`）。 |

## 三個驗證問題（只根據倉庫檔案回答）

1. **這個專案是做什麼的？** 第 9 組的英文單字學習工具，Python 寫在 `VocaBuddy.ipynb`、在 Colab 執行：單字分類總覽、中翻英測驗、HTML 單字卡介面（`README.md`）。
2. **列出所有檔案。**（改動前 `git ls-files` 共 2 個）`README.md`：專案說明、組員、執行方式；`VocaBuddy.ipynb`：cell 0 資料與函式、cell 1 HTML/CSS/JS 介面。
3. **單字資料放在哪個變數？目前有幾個單字？** cell 0 的 `vocabulary`（`VocaBuddy.ipynb:17`），格式 `{分類: {英文: 中文}}`；改動前 **2 個分類、3 個單字**（apple、banana、cat），改動後 3 個分類、6 個單字。

## 小改動的證據

| 檢查 | 結果 |
|---|---|
| `git diff` | Lab 11 當下 `VocaBuddy.ipynb` 只新增 5 行（`"程式"` 分類與 3 個字），metadata 與輸出沒變。之後的分支 diff 另含 Lab 12 的 `shuffle_words()`（7 行） |
| `python3 check_words.py` | `vocabulary 檢查通過，共 3 個分類、6 個單字 ✓` |
| 執行 cell 0 函式 | `exec` cell 0 後 `run_quiz(3, category="程式")` 依序出題迴圈／除錯／變數；`show_summary()` 顯示「程式（3 個）：loop, variable, debug」 |
| 介面 | cell 1 從 `vocabulary` 產生 `words_for_ui`（`VocaBuddy.ipynb:169`），分類選單會自動出現「程式」；⏳ 待組員在 Colab 執行確認 |
