# \[Day1\] Python? 進階?

下一篇: [ \[Day2\] 進階語法 1 - Function and Typing ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day2.md)

---

## 大綱修改聲明

隨著文章內容不段更新，作者意識到原定大綱內容過於複雜，可能導致讀者難以學習，經過作者考量，決定將此次教學內容著重在資料科學方面，並刪減了網路應用相關內容，刪除條目如下

- 網路應用基本概念
- 基礎爬蟲與網頁分析
- 建立自己的 API

並新增了相關條目

- 基礎資料分析與數學
- 認識人工智慧與深度學習
- 基本神經網路
- 基本神經網路實作

對於期待網路方面相關教學的讀者，我至上最深的歉意，但是資料科學也是一個有趣的領域，並且非常具有實用性，筆者在此保證在改動大綱後的內容絕對不會馬虎，絕對做到最頂。

---

這篇進階 Python 教學將會讓你更認識 Python 的語法與一些實作。  
以下為教學內容：

- 進階語法和程式設計觀念
- 基本 OOP(物件導向程式設計) 概念與 Python 函式進階 (如裝飾器等)
- 第三方套件(package)使用
- 專案製作概念 (程式設計師會如何開發專案)
- 基礎資料分析與數學
- 認識人工智慧與深度學習
- 基本神經網路
- 基本神經網路實作

這次的教學範圍包跨了許多應用面的實作，並稍微介紹了物件導向的概念，接著會認識到 Python 的套件庫與使用方式，並介紹到基本的網路概念與建立自己的伺服器和 API，最後會稍微講解人工智慧的基本知識，或許未來還會有機器學習的專題教學。

本系列文章將會採每日更新，並不固定篇數更新至 Github/Medium/NazpBlog 等平臺 以下是系列文章連接將會持續更新，可以收藏本頁以便觀看。

1. [ \[Day1\] Python? 進階? ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day1.md)
2. [ \[Day2\] 進階語法 1 - Function and Typing ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day2.md)
3. [ \[Day3\] 進階語法 2 - function and Decorator ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day3.md)
4. [ \[Day4\] 進階語法 3 - Lambda Function ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day4.md)
5. [ \[Day5\] 進階語法 4 - Python Class & OOP ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day5.md)
6. [\[番外篇\] Python 基礎到底是哪些 窩真的不懂](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Add1.md)
7. [ \[Day6\] 程式應用 1 - Python Package ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day6.md)
8. [ \[Day7\] 程式應用 2 - 初學Numpy ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day7.md)

本系列所有範例程式碼將會全部放在 [Github 這裡](https://github.com/banahaker/python_advanced_tutorial/)，有需要請自行取用。

第一天就沒有任何程式碼實在不是個好示範，所以我們不厭其煩得來寫個 Hello, world

```python
try:
  raise Exception("Hello, World!")
except Exception as e:
  print(str(e))
```

[hello.py](https://github.com/banahaker/python_advanced_tutorial/blob/main/hello.py)

這個範例程式就出現了一個可能之前沒看過的語法，不過未來都會介紹，如果在觀看文章的過程中有發現不懂的概念都可以先 Google 看看，如果有需要都可以用以下方式聯絡我

- Email: lazpytb@gmail.com
- Discord: [Lazp#6012](http://discord.com/users/813904269727236108)
