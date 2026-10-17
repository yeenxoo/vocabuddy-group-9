# PROJECT_RULES.md

給 AI 工具與組員的專案規則。每次修改 `app/` 前先讀這份。

## 這是什麼專案

- VocaBuddy：間隔重複（5 個盒子）背英文單字的網頁 App，純前端，沒有後端或資料庫。
- 學習紀錄只存在瀏覽器 localStorage（`vb-log`、`vb-words`、`vb-day` 等）。
- 本次作業（YTP E2）的程式全在 `app/`；根目錄的 `VocaBuddy.ipynb` 是上一次的 Python 作業，不在本次修改範圍。

## 怎麼啟動與測試

以下指令都在 `app/` 執行：

```bash
# 測試（每一支都要通過，結束碼為 0）
node test_srs.js
node test_csv.js
node check_words.js
# 新增測試檔後，也要列在這裡並一起跑

# 啟動畫面（macOS/Linux 用 python3，Windows 用 py）
python3 -m http.server 8000
# 瀏覽器開 http://localhost:8000
```

`sw.js` 會先讀快取。改了 JS 之後畫面若沒變，到 DevTools → Application 清除 Service Worker 與 Cache Storage 再重新載入。

## 檔案與程式慣例

| 檔案 | 用途 |
|---|---|
| `app/index.html` | 畫面與互動（讀寫 localStorage、呼叫純函式） |
| `app/words.js` | 單字資料 `WORDS`，每筆 `{en:"...", zh:"..."}` |
| `app/srs.js` | 排程純函式 `schedule` 與 `INTERVALS` |
| `app/csv.js` | CSV 匯入的純函式 |
| `app/test_*.js`、`app/check_words.js` | Node 測試，用內建 `assert`，不裝套件 |

- 純函式（`srs.js`、`csv.js`）不碰畫面、不讀時鐘、不改輸入；日期由呼叫者傳入，單位是「天」（整數），不是毫秒。
- 每個 JS 檔結尾保留 `if (typeof module !== "undefined") module.exports = ...`，新增函式就加進這個匯出，不刪除原有的匯出名稱。
- 新增的每個函式上方加一行固定記號：`// 用途：<一句話說明>`
- 單字 `en` 不可重複、`en` 與 `zh` 都不可空白；新增前先檢查是否已存在，已有就跳過。
- 註解與訊息用繁體中文。

## 每次修改的驗收流程

1. 先讀相關檔案，列出計畫（改哪些檔、為什麼、怎麼驗證），等組員回覆「執行」才改。
2. 只改計畫內的檔案，保留既有資料與行為。
3. 改完跑上面的全部測試，貼出實際輸出；沒有跑過的不可寫成「通過」。
4. 若有改到畫面相關的檔案，啟動 HTTP 伺服器，人工確認畫面與 Console 沒有錯誤。
5. 用 `git status` 和 `git diff` 檢查變更；新檔案要先 `git add` 才看得到完整 diff（`git diff --cached`）。
6. commit 由組員看過 diff、review 完成後決定。

## 不能做的事

- 在 `e2/practice` 分支上修改；review 完成後，由組員決定是否合併回 `main`。
- AI 不可自動 commit、合併或 push；這些都由組員決定。
- 不可為了讓測試通過而刪除或放寬既有測試。
- 不可修改 `schedule` 的行為或 `INTERVALS` 的數值，除非任務明確要求。
- 不可加入後端、資料庫、建置工具或 npm 套件。
- 不可把 API key 或任何金鑰寫進檔案。
- 不可抄寫導師範例 repo（`vocabuddy-group-mentor`）裡的成果；所有修改由本組自行完成。
