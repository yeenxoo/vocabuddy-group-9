---
name: add-words
description: 新增或修改 VocaBuddy 單字時使用。使用者說「加單字」「新增單字」「加幾個某主題的字」「新增一個分類」「改單字／改中文意思」「動 vocabulary」都算。包含 VocaBuddy.ipynb 裡 vocabulary 的格式、安全的 notebook 改法、check_words.py 驗證，以及交給組員 commit 的方式。
---

# 新增單字（add-words）

照順序做，每一步都要做到，不可跳過。

1. **先讀格式**：讀 `VocaBuddy.ipynb` 第一個 cell 的 `vocabulary`，格式是 `{分類: {英文: 中文}}`。先確認目前有哪些分類、哪些英文字已經存在。
2. **確認分支**：跑 `git branch --show-current`。如果在 `main`，先停下來問組員要開哪個分支（例如 `feature/add-words-<主題>`），不要直接在 `main` 改。
3. **加在最後**：
   - 主題已有分類 → 加在該分類的最後；沒有 → 在 `vocabulary` 最後新增一個中文分類名稱。
   - 英文一律小寫、去頭尾空白；中文用繁體。已存在的英文（任何分類）就跳過，並告訴組員跳過了哪些。
   - 不要重排、不要改既有的字。
   - 用 Python 的 json 讀寫 notebook，只改 cell 0 的 `source`：`json.dumps(nb, indent=2, ensure_ascii=False) + "\n"`。不要手動編輯 .ipynb 的 JSON 文字，也不要動輸出與 metadata。
4. **驗證**：跑 `python3 check_words.py`，必須看到「檢查通過」且結束碼 0。失敗就修資料，不可改 `check_words.py` 來讓它通過。另外自己看一眼中文意思是否正確——腳本只檢查格式，不檢查翻譯對不對。
5. **給組員看**：跑 `git status` 與 `git diff`，確認只改了 `VocaBuddy.ipynb`。回報新增的單字（英文→中文、分類）、跳過的單字、`check_words.py` 的實際輸出，並附上建議的 commit 訊息：`feat: 新增 N 個「主題」單字`。
6. **不要 commit、不要 push**：commit、push 與開 PR 都由組員看過 diff 後自己做。
