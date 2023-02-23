# \[Day4\] 進階語法 3 - Lambda Function

上一篇: [ \[Day3\] 進階語法 2 - function and Decorator ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day3.md)
下一篇: [ \[Day5\] 進階語法 4 - Python Class & OOP ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day5.md)

Lambda，波長，是波速與頻率比值。喔抱歉跑錯棚，今天不是教物理，要講的是 Python 的 Lambda Function，也就是匿名函數。

### Lambda 幹啥呢

Lambda Function，匿名函數是一種函數類型，他不需要定義一個名字，只有一行的內容，很適合用於小型、臨時性的計算，馬上就來個範例

```python
lambda v, f: v / f
```

就一行，這麼簡單，定義了一個匿名函數，函數傳入兩個參數 `v` 和 `f` 回傳 `v/f`。可是執行怎麼都沒有出現東西，因為你沒有把他 print 出來，他只會單純定義一個匿名函數，所以可以這樣做，

```python
print((lambda v, f: v / f)(3, 2))
```

他就會印出

```py
2.5
```

Lambda Function 在沒有執行的時候是會回傳整個函數地所以可以這樣使用

```python
lambda_func = lambda v, f: v / f
print(lambda_func(4, 2))
```

執行輸出結果

```py
2.0
```

### 所以她到底可以幹嘛

他可以再使用某些函數是當作函數傳入，例如 `map()`，可能沒有聽過這個函數，他是一個可以迭代串列(List)並對其值做出改變的函數，先來個範例

```python
def multiply(x):
    return x * 2

a = [1, 2, 3, 4, 5]
result = map(multiply, a)
print(list(result))
```

簡單來說就是先定義了一個 `multiply` 函數他會回傳傳入參數值的兩倍，接著宣告一個 List 變數 `a`，接著宣告一個變數 `result` 其內容為 `map` 函數過後的結果，map 函數會走訪串列 `a` 的所有內容並且把值傳入 `multiply` 函數並且把值改成其回傳值，所以這個範例輸出會是

```python
[2, 4, 6, 8, 10]
```

理解了 `map` 如何使用之後就可以把 Lambda Function 融入他了

```python
a = [1, 2, 3, 4, 5]
result = map(lambda x: x*2, a)
print(list(result))
```

這樣的輸出結果也會跟前一個範例一樣，但是少了許多程式碼，是不是很方便呢。

### 這東西也太棒了吧，還不用爆

喔不這東西還是有缺點的，像是他容易讓程式碼變得難以閱讀，導致別人甚至兩個禮拜後的自己看不太懂，所以要斟酌使用。

## 結語

今天的內容，Lambda Function 應該看起來比較容易學習對吧，以後可以善用他，接下來的教學將會進入 OOP 的介紹，不過內容可能跟你想的不太一樣，敬請期待。
