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


o = Apple("Big Apple", 345.678, "Red")
print(o.get_color())