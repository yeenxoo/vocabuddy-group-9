# Lab 12 驗收紀錄：專案指示檔 CLAUDE.md

驗證日期：2026-10-17｜對照實驗用 `claude -p` 開全新 session（等於教材的「清空工作階段」），在 repo 的暫存副本執行，只放行 `Read,Grep,Glob`，模型 `claude-sonnet-5-5`。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 根目錄有專案指示檔，檔名符合工具 | ✅ | `.claude/CLAUDE.md`（Claude Code 讀根目錄或 `.claude/` 底下的 `CLAUDE.md`）。組員各用各的工具：Claude Code 的設定放 `.claude/`，Copilot 的放 `.github/`，所以沒有放根目錄。對照實驗原本在根目錄跑，搬家後重跑實驗組確認仍生效（見下方）。 |
| 2 | 五個段落齊全，每一條你都認同 | ⏳ | 五段：這是什麼專案／怎麼跑起來／程式碼慣例／協作規矩／不要做的事。規矩來自 notebook 現有寫法與舊的 `PROJECT_RULES.md`（commit `768b228`）。**待組員逐條刪改後定稿。** |
| 3 | 總長度在 60 行以內 | ✅ | `wc -l .claude/CLAUDE.md` → 35。 |
| 4 | 對照實驗驗證它真的生效 | ✅ | 見下方。 |
| 5 | issue → 分支 → PR → review → merge 走完一輪 | ⏳ | 目前在分支 `feature/agentic-setup`，尚未 commit；待組員開 issue、commit、發 PR、review 後合併。 |

## 對照實驗

同一句話，兩個全新 session：

> 在 VocaBuddy.ipynb 第一個 cell 加一個 shuffle_words() 把單字順序打亂。請先讀檔，然後把要新增的程式碼與要放的位置印出來給我，我自己貼進去。

| | 對照組（沒有 CLAUDE.md） | 實驗組（有 CLAUDE.md） |
|---|---|---|
| docstring | `"""回傳打亂順序後的所有單字，格式與 all_words() 相同。"""` | `"""用途：回傳打亂順序後的所有單字，格式與 all_words() 相同，不會改動 vocabulary。"""`，並說明「第一行照 CLAUDE.md 寫成 `用途：`」 |
| 函式設計 | 用 `all_words()` 的副本洗牌、回傳 | 相同 |
| 驗證建議 | 無 | 主動建議跑 `python3 check_words.py`，並誠實說「我沒有執行過這段程式」 |
| 動到別的檔 | 無 | 無 |

**判讀**：辨識規矩是「docstring 第一行寫 `用途：`」。notebook 原本的 docstring 都沒有這個前綴，所以模型照抄現狀不會自然做到；實驗組提示裡一個字都沒提就做到了。每組只跑一次，樣本小，但這個差異只可能來自 CLAUDE.md，結果支持指示檔生效。

**搬家後重跑**：組員決定各用各的工具（Claude Code 用 `.claude/`、Copilot 用 `.github/`），`CLAUDE.md` 移到 `.claude/CLAUDE.md`。在副本中先拿掉已貼入的 `shuffle_words()`、刪掉 `labs/`（避免它看到答案），同一句話再跑一次全新 session：docstring 仍是 `"""用途：回傳打亂順序後的單字清單，格式同 all_words()，不會改動 vocabulary 本身。"""`，並說「docstring 第一行照 CLAUDE.md 寫成 `用途：`」，也建議跑 `check_words.py`。新位置確認生效。

## 實驗產物

`shuffle_words()` 照實驗組的草稿貼進 cell 0（`VocaBuddy.ipynb:44`）。驗證：5 次呼叫張數與單字集合都不變、`vocabulary` 沒被改動、5 次中 5 次順序改變；`python3 check_words.py` → `vocabulary 檢查通過，共 3 個分類、6 個單字 ✓`。
