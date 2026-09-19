# vocabuddy-group-9

## 小組名稱

耶耶耶gobackgoback

## 組員姓名

范翔皓、李品宏、黃昱叡、黃浩銓、殷家祥

## 組員的 GitHub 帳號

@z04cl4、@peterooo777、@yeenxoo、@tyellow07、@Xiang0909

## 專案簡介

VocaBuddy 是一個簡單的英文單字學習工具，使用 Python 製作，適合用來整理單字、查看單字分類，並透過小測驗加強記憶。使用者可以在 Google Colab 中直接執行程式，不需要額外安裝複雜的環境。

## 組員分工

- 黃昱叡：Github repository建立, README撰寫
- 李品宏：新增單字, 專案建立
- 殷家祥：單字測驗功能建立, README撰寫

## 本次新增的單字與功能

- 新增 `apple（蘋果）`、`banana（香蕉）`、`cat（貓咪）` 三個單字。
- 將單字分為「水果」和「動物」分類，並顯示每個分類的單字數量。
- 顯示目前單字總數與所有分類內容。
- 新增簡單的中文翻英文隨機測驗。
- 記錄答對與答錯的題目數量，並在總覽中顯示答題紀錄。
- 提供 `add_word()` 函式，能新增單字、中文意思與分類。
- 改善程式輸出格式，讓總覽與測驗結果更容易閱讀。
- 使用 `IPython.display.HTML` 搭配 HTML、CSS、JavaScript 建立簡約且具響應式的可視化介面。
- 新增單字卡翻面功能，可查看英文與中文意思。
- 提供上一張、下一張、隨機單字與分類篩選功能。
- 使用頁籤切換「單字卡」、「單字測驗」與「單字分類」。
- 測驗介面提供分類選擇、題數設定、進度條、Enter 送出答案與下一題按鈕。
- 即時顯示答對題數、答錯題數與目前正確率。
- 支援鍵盤操作、焦點提示、手機版響應式排版與減少動畫設定。

## Google Colab 開啟連結

[https://colab.research.google.com/github/yeenxoo/vocabuddy-group-9/blob/main/VocaBuddy.ipynb?hl=zh-tw](https://colab.research.google.com/github/yeenxoo/vocabuddy-group-9/blob/main/VocaBuddy.ipynb?hl=zh-tw)

## 程式執行方式

### 使用 Google Colab

1. 開啟上方的 Google Colab 連結。
2. 依序執行 notebook 中的兩個 Python cell。第一個 cell 載入單字資料與核心函式，第二個 cell 顯示 HTML/CSS/JavaScript 操作介面。
3. 在「單字卡」頁籤中點擊卡片翻面，或使用「上一張」、「下一張」、「隨機單字」切換單字。
4. 在「單字測驗」頁籤選擇分類與題數，按下「開始測驗」，輸入英文答案後按「確認答案」；也可以直接按 Enter 送出。
5. 在「單字分類」頁籤查看所有分類與單字。
6. 也可以使用下列 Python 指令開始文字版隨機單字測驗：

```python
run_quiz()
```

7. 若只想測驗指定分類，可以使用：

```python
run_quiz(category="水果")
```

8. 若要新增單字，可以使用：

```python
add_word("book", "書", "物品")
show_summary()
```

### 在本機執行

使用支援 Jupyter Notebook 的環境開啟 `VocaBuddy.ipynb`，依序執行兩個 Python cell 即可。程式使用 Python 內建的 `random`、`json` 模組，以及 `IPython.display` 顯示 HTML 介面；若本機尚未安裝 IPython，可執行 `pip install ipython`。
