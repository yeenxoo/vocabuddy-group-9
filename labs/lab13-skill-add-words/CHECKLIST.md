# Lab 13 驗收紀錄：第一個技能 add-words

驗證日期：2026-10-17｜正負測試用 `claude -p` 開全新 session（在 repo 的暫存副本執行），`--output-format stream-json --verbose` 錄下每個工具呼叫，模型 `claude-sonnet-5-5`。測試產物（天氣單字）只留在暫存副本，沒有進 repo。
狀態標記：✅ 通過｜⏳ 待補｜❌ 未通過

| # | 教材驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 技能資料夾與 SKILL.md 建好，frontmatter 有 name 與 description | ✅ | `.claude/skills/add-words/SKILL.md`，frontmatter 只有 `name`、`description`。 |
| 2 | description 寫「什麼時候該用」 | ✅ | 「新增或修改 VocaBuddy 單字時使用。使用者說『加單字』『新增單字』『加幾個某主題的字』『新增一個分類』…都算。」 |
| 3 | 正面測試通過 | ✅ | 見下方。 |
| 4 | 負面測試通過 | ✅ | 見下方。 |
| 5 | 技能已進版控，經 PR 合併 | ⏳ | 待組員 commit、發 PR、review 後合併。 |

## 和教材不同的地方

- 教材第 5 步是「用規定訊息 commit」。本組規矩是 AI 不 commit（`CLAUDE.md`「不要做的事」第 1 條），所以改成「給出建議的 commit 訊息，交給組員 commit」。
- 新增第 2 步「在 `main` 就停下來問」，以及「用 json 只改 cell 0 的 `source`」——notebook 是 JSON，手改容易弄壞或把輸出一起改掉。
- 驗證工具是本組自己的 `check_words.py`（Python，用 ast 讀出 `vocabulary`，不執行 notebook）。

## 正面測試：「幫我加三個天氣主題的單字。」

放行工具：`Read,Glob,Grep,Skill,Bash(python3:*),Bash(git status:*),Bash(git diff:*),Bash(git branch:*),Bash(git log:*)`（不含 commit、push）。

| 步 | 工具 | 內容 | 對應技能步驟 |
|---|---|---|---|
| 1 | `Skill` | `add-words` | 觸發 |
| 2 | `Bash` | `git branch --show-current` ＋ 用 ast 讀出 `vocabulary` | 1 讀格式、2 確認分支 |
| 3 | 文字 | 照 CLAUDE.md 先列計畫：新增分類「天氣」：rain→雨、sunny→晴朗的、storm→暴風雨，不 commit，等同意 | — |
| 4 | （組員回覆「同意，照計畫做。」，`--resume` 同一個 session） | | |
| 5 | `Bash` | python json 讀寫，只改 cell 0 `source`，加在 `vocabulary` 最後 | 3 加在最後 |
| 6 | `Bash` | `python3 check_words.py` → `vocabulary 檢查通過，共 4 個分類、9 個單字 ✓` | 4 驗證 |
| 7 | `Bash` | `git status --short`、`git diff` | 5 給組員看 |
| 8 | 文字 | 回報單字、檢查輸出、建議訊息 `feat: 新增 3 個「天氣」單字`；主動指出 notebook 有它之前就存在的未提交修改；「我沒有 commit 或 push」 | 6 不 commit |

事後確認：暫存副本的 `git log -1` 仍是 `de14ad6`（沒有新 commit），diff 只有 `source` 行。

## 負面測試：「幫我把卡片的圓角改大一點。」

工具呼叫只有 `Grep border-radius`，指出 `.vb-card` 的 `border-radius: 14px`（`VocaBuddy.ipynb:193`），提出改 cell 1 的計畫等同意；**沒有 `Skill`、沒有跑 `check_words.py`、沒有改檔**。它另外發現 cell 1 已存的輸出（第 105～131 行）也有同一段 CSS，重新執行 cell 1 才會更新。
