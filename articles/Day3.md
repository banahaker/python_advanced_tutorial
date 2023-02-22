# \[Day3\] 進階語法 2 - function and Decorator

上一篇:[ \[Day2\] 進階語法 1 - function and Typing ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day2.md)
下一篇: [ \[Day4\] 進階語法 3 - Lambda Function ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day4.md)

看完昨天的文章應該比較了解不同型別系統的差異，越學越多程式相關知識之後就會像這樣開始聊解程式運作系統的概念，今天我們來講點輕鬆的 - Decorator (裝飾器)。

### 先認識認識 Python 的 function

Python 的 function 大家應該都已經熟悉如何使用了，先拿昨天的範例程式碼來開頭

```py
def func(c: int) -> int:
    print(c)
    return c+1
```

這裡的 `func` 就是個函數，在 Python 中 function 是屬於`一等公民(First-Class Citizens)`存在的，甚麼是一等公民呢，他能夠像一般的變數一樣做一些類似的操作，像是複製

```py
def func(c: int) -> int:
    print(c)
    return c+1;

func_2 = func
print(func_2(123))
```

在這個範例中，我新增了一個 `func_2` 變數，並傳入了 `func` 進去，此時`func`的內容就被複製到 `func_2` 裡面去了，並且執行結果與直接執行 `func` 一樣都是

```
123
124
```

除了是一等公民以外呢，函數還有許多有趣的小功能，我們來看看！首先，我們可以把它刪掉

```py
def func(c: int) -> int:
  return c+1
del func
func()
```

使用`del`這個關鍵字就可以把它給刪掉，上面這段程式碼其實拿去執行是會出錯的，因為你不能把它刪掉又執行他。  
接著再來看看，我們可以在函數裡面定義一個新的函數像這樣

```py
def func(c: int) -> int:
  def plus(a: int) -> int:
    return a + 1
  print(plus(c))
  return c+2

print(func(123))
```

這段的執行結果會是

```
124
125
```

熟悉 function 的人應該馬上就能了解，接著更炫砲的來了喔，還記得上面 `func` 函數的參數 `c` 嗎，那你有沒有想過參數搞不好可以放函數，可能聽不太懂，我們馬上來看範例:

```py
def func(f) -> None:
    f()

def hello():
    print("hello, world")

func(hello)
```

這個範例裡面我們可以看到將 `hello` 這個 function 當成了一個參數傳入了 `func` 這個函數裡面，接著執行他，所以函數在 Python 中不僅可以複製還可以當成參數傳入函數，但要注意的是，這種概念只有在部分語言中存在，許多語言如 C 都是不支援這樣的用法的喔(但有個東西叫做 function Pointer 有興趣的可以看我[這篇文章](https://medium.com/@lazpytb/c%E8%AA%9E%E8%A8%80-%E5%87%BD%E5%BC%8F%E6%8C%87%E6%A8%99-funtion-pointer-526305772174))。

### 裝飾器，雖然可能不好看，但是必須知道

首先我們來看看基本的裝飾器

```py
def decorator(func):
    def wrapper(x):
        func(x)
    return wrapper

def foo(x: str) -> None:
    print(x)

bar = decorator(foo)
bar("hello")
```

看起來可能有點複雜，不過我們一個一個來解釋，首先定義了一個函數`decorator`，傳入一個函數參數 `func` 接著在定義一個 `wrapper`函數並且回傳，可能聽起來有雜，但口語一點來講就是創建一個 `decorator` 函數，而他的工作就是生成一個 `wrapper` 函數然後這個 `wrapper` 裡面會執行 `func` 這個函數，最後把生成好的東西回傳。像 `decorator` 這樣的函數我們稱為 裝飾器(Decorator)。接著我們繼續看接下來的程式碼，定義一個 `foo` 函數負責印出傳入的參數，最後我們創建一個`bar`他接收了 `decorator` 回傳的 `wrapper`(還記得前面說函數可以複製、賦值吧)，而那個`func`正是 `foo`。最後統整一下，這樣的程式碼會輸出

```
hello
```

### 好甜好甜，裝飾器的語法糖

上面的寫法可能有些複雜，不過是可以藉由語法糖作簡化的

```python
def decorator(func):
    def wrapper(x):
        func(x)
    return wrapper

@decorator
def foo(x: str) -> None:
    print(x)

foo("hello")
```

語法糖是一種讓程式簡化的東西，像是 python 中的裝飾器語法糖就能把程式簡化，範例中，利用 `@` 符號讓`foo` 直接帶入 `decorator` 中並且重新包裝到 `foo` 就能達到跟上面範例一樣的結果。

## 結語

到此應該能比較聊解裝飾器在 Python 中的用法了，在未來可能會遇到複雜程式，都能使用該概念解決。
