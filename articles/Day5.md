# \[Day5\] 進階語法 4 - Python Class & OOP

上一篇: [ \[Day4\] 進階語法 3 - Lambda Function ](https://github.com/banahaker/python_advanced_tutorial/blob/main/articles/Day4.md)

哈囉各為大家好，今天去學校的 Class 上課感覺如何？應該還不錯，那我們今天就來講 Python Class 吧！

### OOP, Object-oriented programming

如果有常在看程式設計相關的文章的話應該就有可能會注意到 OOP 這個名詞，而她的中文是`物件導向程式設計`，而物件導向又是甚麼呢？OOP 是一種常用的程式設計範式，它將程式中的資料（Data）和方法（Method）封裝成物件（Object）。物件可以透過繼承（Inheritance）、封裝（Encapsulation）和多型（Polymorphism）等特性進行模組化、重複使用及擴展。OOP 提供了一種更直觀、易於理解的程式設計方法，並且有助於提高程式碼的可讀性、可維護性和可擴展性。目前許多現代程式語言都支援 OOP，如 Java、C++、Python 等。上面看到了許多新名詞我來一一介紹他。

### 封裝、繼承、多型

這三個概念是 OOP 最核心的三個概念，首先我們講到封裝(Encapsulation)，封裝是 OOP 很重要的概念，具體來說他就是把每個功能包裝成一個物件或是所謂的類別(Class)，透過封裝，我們可以將物件的實現細節隱藏起來，只開放必要的介面給外界使用，進而增強程式碼的可讀性、可維護性和可擴展性。此外，封裝還能提高程式碼的安全性，因為外部程式碼無法直接訪問物件的內部狀態，只能透過介面來進行操作。在實現封裝時，一般使用 private、protected、public 等訪問修飾符來控制對內部狀態和方法的訪問權限。而 getter 和 setter 方法則是對外暴露介面，用於讀取和修改封裝的內部狀態。

來看看 Python 如何定義一個 Class 物件

```python
class Fruit:

    def __init__(self, nameAtr: str, weightAtr: float) -> None:
        self.name = nameAtr
        self.weight = weightAtr

    def get_weight(self) -> float:
        return self.weight
```

就像這樣就製作了一個簡單的物件類型，一個物件類型你可以把他當做一個自訂的型別，首先我們看到裡面定義的 `__init__` 函數，他是所謂的建構函數(Class Constructor)，他會在我們宣告這個類別的變數實會需要輸入的，那如何宣告一個 Fruit 類別的變數呢

```python
class Fruit:

    def __init__(self, nameAtr: str, weightAtr: float) -> None:
        self.name = nameAtr
        self.weight = weightAtr

    def get_weight(self) -> float:
        return self.weight

o = Fruit("orange", 12.3)
```

就像這樣，我們定義了一個新的 `o` 變數，然後他使用了 Fruit 類別來宣告，然後在使用的時候傳入了兩個參數 `("orange", 12.3)`，分別對應到上面建構函數的 `(nameAtr: str, weightAtr: float)`。咦？等等好像哪裡怪怪的，那個 `self` 是甚麼，他是一個變數，代表了實體物件的參考(Reference)，也就是目前的物件。這個 self 就是告訴 Class 目前是在設定哪一個物件的屬性。所以範例中的意思就是此物件的`name`屬性等於傳入的`nameAtr`屬性值，`weight`亦之。所以 `self.name` 就是指說這個物件裡面有個內容物叫做 `name`，可以用以下方法取用

```python
print(o.name)
```

這就會印出 `orange`。接著，類別中除了可以有自己的內容物之外也可以有自己的方法，定義方法就是上面範例的 `def get_weight(self)`，而這個 `self` 也是參照到他自己，所以這個方法會回傳他自己的重量，呼叫這個方法的方式如下

```py
class Fruit:

    def __init__(self, nameAtr: str, weightAtr: float) -> None:
        self.name = nameAtr
        self.weight = weightAtr

    def get_weight(self) -> float:
        return self.weight

o = Fruit("orange", 12.3)
print(o.get_weight())
```

他就會正確印出

```
12.3
```

知道甚麼是封裝之後我們就來看看繼承(Inheritance)，繼承簡單來講就是可以創建一個子類別，他會繼承父類別的所有特性，用講的難以明白，咱們來個範例

```python
class Fruit:

    def __init__(self, nameAtr: str, weightAtr: float) -> None:
        self.name = nameAtr
        self.weight = weightAtr

    def get_weight(self) -> float:
        return self.weight

class Apple(Fruit):
    pass

a = Apple("Big Apple", 345.678)
print(a.get_weight())
```

可以看到，我又再定義了一個新的類別 `Apple` 不過我在後面加上了 `(Fruit)`，意即繼承 Fruit，因此就算使用 `Apple` 宣告了 `a` 變數都還是可以正常使用建構函數以及裡面的 `get_weight` 方法，這就是所謂的繼承，當然你也可以補充東西到子類別

```python
class Apple(Fruit):

    def __init__(self, nameAtr: str, weightAtr: float, colorAtr: str) -> None:
        super().__init__(nameAtr, weightAtr)
        self.color = colorAtr

    def get_color(self):
        return self.color

```

就像這樣就可以幫 Apple 的建構函數再新增一個 `color` 的初始化，那個 `super().__init__()`是甚麼呢，他其實就是使用到父類別方法時，可以就由 `super()` 來指向父層，就可以對父層函數內容進行修改。

最後我們來談談多型(Polymorphism)，多型是在物件導向中很重要的概念，他讓不同型態的物件可以有更好的適配性，做出不同的反應，在 Python 中可能會覺得多型的概念並不明確，可是 Python 是確確實實有多型的概念的，我們馬上來試試看

```python
class Fruit:

    def __init__(self, nameAtr: str, weightAtr: float) -> None:
        self.name = nameAtr
        self.weight = weightAtr

    def get_weight(self) -> float:
        return self.weight


class Apple(Fruit):

    def __init__(self, nameAtr: str, weightAtr: float, colorAtr: str) -> None:
        super().__init__(nameAtr, weightAtr)
        self.color = colorAtr

    def get_color(self):
        return self.color

    def get_weight(self) -> str:
        return f"{self.weight} kg"


class Orange(Fruit):

    def __init__(self, nameAtr: str, weightAtr: float,
                 leafCountAtr: int) -> None:
        super().__init__(nameAtr, weightAtr)
        self.leafCount = leafCountAtr

    def get_weight(self) -> str:
        return f"{self.weight} g"
```

就像這樣，一樣是 Fruit，也都一樣有 `get_weight` 這個方法，可是不同的水果確有不同的表現方式，像是 `Apple` 就會顯示公斤數，`Orange` 就會顯示公克數，這樣針對不同東西的適應，就是所謂的多型。

鴨子定型，這是一個在 OOP 中常見的一個名字，他很完美的詮釋了所謂的多型

> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

只要物件的屬性和方法類似於其他物件，那他們就是同一類別，這樣的應用在 Golang 中模擬 OOP 也存在。

## 結語

今天介紹了大部分的 OOP 概念，但其實 OOP 並不是一個這麼簡單的東西，還有許多東西可以探討，雖然 OOP 看起來非常的好用或是很酷，也是有許多缺點的，像是容易導致過度的抽象思考設計，還有難以閱讀等問題，都很容易導致程式開方上的困難，所以更多時候我們會選擇使用 FP 來取代。
