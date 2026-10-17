# Lab 14 驗收紀錄：子代理 code-reviewer

驗證日期：2026-10-17｜子代理實跑用 `claude -p` 開全新 session（在 repo 的暫存副本執行），只放行 `Read,Grep,Glob,Agent,Bash(git diff:*)`，`--output-format stream-json --verbose` 錄下主對話與子代理（`parent_tool_use_id`）各自的工具呼叫，模型 `claude-sonnet-5-5`。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 子代理建好，工具權限限制為唯讀 | ✅ | `.claude/agents/code-reviewer.md`：`tools: Read, Grep, Glob`、`permissionMode: plan`；沒有 Bash（Bash 能繞過唯讀）。實跑時子代理只呼叫了 `Grep` ×1、`Glob` ×1。 |
| 2 | 對真實 diff 跑過，輸出符合格式（含行號） | ✅ | 主對話先跑 `git diff main -- . ':!.claude/agents'`（Lab 11～13 的全部變更，8 檔 235 行），把全文放進提示交給子代理；回報 6 則，每則 `[嚴重度] 檔名:行號 — 問題 — 建議`，依嚴重度排序，最後一行「以上為機器初審，仍需人工 review。」。暫存副本事後 `git status` 沒有任何檔案被改。 |
| 3 | 你先自己審過，才看它的報告 | ⏳ | **待組員**：先用四面向（正確性／安全性／可讀性與慣例／測試與證據）審 `git diff main`，寫下發現，再看下方報告。 |
| 4 | 四格比較表填完，結論寫進 PR 留言 | ⏳ | 機器那兩格已填；「兩邊都抓到」「只有你抓到」待組員審完後填，再貼到 PR 留言。 |
| 5 | merge 是你按的，說得出為什麼可以合 | ⏳ | 待組員。 |

## 子代理報告原文

```
[中] check_words.py:30 — `ast.literal_eval` 遇到同一分類內重複的英文 key 時，後面的會靜默覆蓋前面的，所以「重複單字」只在跨分類時才查得到。 — 改用 `ast.Dict` 節點逐一檢查 key，或在載入時偵測同一分類內的重複 key 並回報。
[中] labs/lab11-agentic-setup/CHECKLIST.md:24 — 寫「`VocaBuddy.ipynb` 只新增 5 行」，但這個分支的 notebook diff 還含 `shuffle_words()`（約 7 行），證據已和實際 diff 不符。 — 改成「新增分類 5 行＋`shuffle_words` 7 行」，或註明這是 Lab 11 當下的狀態。第 12 行的「待組員看過 `git diff`」也要提醒 diff 含 Lab 12 的產物。
[中] labs/lab12-project-instructions/CHECKLIST.md:11 — 分支 `lab11-14/agentic-setup` 不符 `CLAUDE.md` 的命名規則（`feature/`、`fix/`、`docs/`）。 — 發 PR 前改名，例如 `docs/agentic-setup`，或在 `CLAUDE.md` 補上這類分支的規則。
[低] labs/lab12-project-instructions/CHECKLIST.md:26 — 「證明指示檔生效」說得太滿，每組只跑一次，樣本太小。「辨識規矩」似乎是打錯字，應該是「關鍵差異」。 — 改成「單次對照，結果支持指示檔生效」，或多跑幾次再下結論，並修正用詞。
[低] labs/lab12-project-instructions/CHECKLIST.md:30 — 寫「`check_words.py` 通過」，但沒有貼實際輸出，而 `CLAUDE.md` 要求貼出實際輸出。 — 補上 `vocabulary 檢查通過，共 3 個分類、6 個單字 ✓` 這類實際輸出。
[低] VocaBuddy.ipynb:44 — `shuffle_words()` 是實驗產物，沒有任何呼叫端，目前是未使用的程式碼。 — 在 PR 說明講清楚是 Lab 12 的示範；若不打算用，就不要併入 `main`。

以上為機器初審，仍需人工 review。
```

## 四格比較表

| 類別 | 觀察 |
|---|---|
| 兩邊都抓到的 | ⏳ 待組員審完後填 |
| 只有它抓到的 | 6 則中 5 則成立。最有價值的是 ①：`check_words.py` 用 `literal_eval` 讀字典，同分類內重複的 key 會被靜默吞掉，「不可重複」只做到一半——這是真 bug，寫程式的人自己的測試也沒抓到。其餘是文件和實際狀態不一致（②⑤）、分支名違反自己寫的規矩（③）、結論說太滿（④ 前半）。 |
| 只有你抓到的 | ⏳ 待組員審完後填 |
| 它抓錯的 | ④ 後半：「辨識規矩似乎是打錯字」——這是教材 Lab 12 的用語，它不知道教材背景。⑥「`shuffle_words()` 沒有呼叫端」本身是事實，但教材本來就保留實驗產物，是流程判斷，不是錯誤。 |

## 採納與不採納（AI 的初步判斷，待組員確認）

| 建議 | 處置 | 改了什麼 |
|---|---|---|
| ① 同分類重複 key | 採納 | `check_words.py` 新增 `duplicate_key_errors()`，從 ast 節點檢查重複的分類與英文；反例（同分類兩個 `cat`、`Dog`、中文寫成 `Cat`）三則都擋下，結束碼 1 |
| ② Lab 11 證據過期 | 採納 | 註明「Lab 11 當下」與之後的 diff 另含 `shuffle_words()` |
| ③ 分支名 | 採納 | `git branch -m` 改成 `feature/agentic-setup` |
| ④ 說太滿／用詞 | 前半採納、後半不採納 | 改成「樣本小，但結果支持指示檔生效」；「辨識規矩」是教材用語，保留 |
| ⑤ 沒貼實際輸出 | 採納 | 補上 `check_words.py` 實際輸出 |
| ⑥ `shuffle_words()` 未使用 | 不採納，交給組員 | 是 Lab 12 的實驗產物；要不要併入 `main` 由組員在 PR 決定 |

## 量到的東西

- 機器初審抓得到：程式的邊界漏洞（重複 key）、文件和實際 diff 不一致、違反自己寫的規矩、沒附證據的「通過」。
- 機器初審抓錯的：需要背景才懂的事（教材用語、教材為什麼保留實驗產物）。
- 唯讀子代理跑不了 `git diff`，所以由主對話先取 diff 再交給它；主對話這次只負責轉交，沒有自己審。
