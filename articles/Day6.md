# \[Day6\] 程式應用 1 - Python Package

上一篇: [ \[Day5\] 進階語法 4 - Python Class & OOP ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day5.md)  
下一篇: [ \[Day7\] 程式應用 2 - 使用 Numpy ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day7.md)

在前五天，我們複習了一些重要概念，也學習了一些新觀念，從今天開始就要進入實作環節了，進到程式應用開發的領域，在出發之前，我們必須先認識所謂的 Package。

### Package 是甚麼？可以幹嘛？

還記得我們之前在寫 Python 程式的時候，會用到一些內建的函數像是 `range`，或是之前介紹到的 `map` 函數，他們都是屬於 Python 標準函式庫中的功能，然而除了這些函數之外，Python 還有許多已經包你包裝好的函數，但他們沒辦法直接使用，你需要把他們連結進到自己的程式碼當中，大概像這樣

```python
import <package_name>
```

使用 `import` 關鍵字就能把那個套件(package)引入到你的程式中。等等，甚麼是套件？可以理解為它是一個包裝盒，裡面放著一些已經寫好的函數讓你可以很方便的使用。

### 實用的內建套件

Python 預設就有許多套件可以用，我們來用用看。首先我們來看看 `math` 這個套件，它提供了提供了各種數學函數，例如三角函數、指數函數、對數函數、階乘等。以下是使用 math 套件計算正弦值的範例：

```python
import math

x = math.sin(2*math.pi)
print(x)
```

它就會輸出

```python
-2.4492935982947064e-16
```

當然，它不只是這個功能還有許多功能，以下範例([範例程式碼](https://github.com/banahaker/python_advanced_tutorial/blob/main/package.py))

```python
import math

# 計算正弦值
x = math.sin(math.pi / 2)
print(x)

# 計算平方根
y = math.sqrt(16)
print(y)

# 圓周率
pi = math.pi
print(pi)

# 自然對數底數
e = math.e
print(e)

# 計算階乘
c = math.factorial(5)
print(c)

# 計算最大公約數
d = math.gcd(12, 18)
print(d)

# 計算對數
z = math.log(10)
print(z)

# https://github.com/banahaker/python_advanced_tutorial/blob/main/package.py
```

這個範例的輸出會是

```py
1.0
4.0
3.141592653589793
2.718281828459045
120
6
2.302585092994046
```

除了 `math` 以外，我們還有其他的套件像是 `random`

```python
import random

x = random.randint(1, 10)
print(x)
```

像這樣就可以輸出一個 1~10 範圍的隨機整數

```python
3
```

除此之外也有相當多的功能，可以自己試著上網查查看資料

### 內建的套件實在是不太夠用

雖然說 Python 內建的套件已經有非常多樣化了，但仍還有許多功能尚未被實作，或是簡化，因此就出現了第三方套件，也就是非官方開發的套件，讓開發更有效率。我們要使用他們就必須使用一些套件管理工具(Package Manager)，而 Python 內建且預設的套件管理工具正是 `pip`，我們來看看怎麼使用。(以 `numpy` 這個知名第三方套件為例)

首先，Python 套件是一組相關的模組，可以在您的程式碼中重複使用，以便更有效率地編寫和組織程式碼。Python 有數千個可用的套件，您可以使用其中的一個或多個來完成您的任務。

以下是使用 Python 套件的一些基本步驟：

#### Step 1. 安裝套件

要使用 Python 套件，您需要先安裝它們。可以使用 Python 內建的套件管理器 pip 來安裝大部分套件。例如，如果要安裝 numpy 套件，可以使用以下命令：

```bash
pip install numpy
```

#### Step 2. 引入套件

這步驟上面已經又使用過了就像是這樣

```py
import numpy
```

但有時候套件名稱太長或是不易鍵入，可以使用別名來簡化匯入的過程：

```py
import numpy as np
```

使用 `as` 關鍵字可以幫套件取暱稱

#### Step 3. 接著就能使用套件裡的功能了

像這樣就能使用了

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```

執行之後就能夠成功輸出

```python
[1 2 3]
```

關於 numpy 的詳細用途，以後會再做介紹。

## 結語

今天介紹了之後開發中一定會用到的功能，package，接下來我們就會慢慢進入到開發的環節了。
