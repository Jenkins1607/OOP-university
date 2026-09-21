"""
Класс разных фигур 
для дальнейших операций
над ними
"""
from math import pi
import numpy as np
from matplotlib.patches import Polygon

class Figure:
    def __init__(self) -> None:
        pass 


    def getCenter(self) -> tuple[float, float]:
        pass

    def getFunc(self) -> tuple[list[float], list[float]]:
        pass

    @property
    def area(self) -> float:
        pass

    @property
    def name(self) -> str:
        return self.__class__.__name__

class Rectangle(Figure):
    def __init__(self, w=5, h=10, x0=0, y0=0) -> None:
        super().__init__()
        self.w = w # ширина
        self.h = h # высота
        
        # координаты левого нижнего угла 
        self.x0 = x0 
        self.y0 = y0

        self.parameters = [f"width: {self.w}", f"height: {self.h}"]

    def getCenter(self) -> tuple[float, float]:
        x_center = (self.x0 + self.x0 + self.w) / 2
        y_center = (self.y0 + self.y0 + self.h) / 2

        return (x_center, y_center)

    def getFunc(self) -> tuple[list[float], list[float]]:
        """Возвращает функцию в параметризованном виде"""
        x = [self.x0, self.x0, self.x0 + self.w, self.x0 + self.w, self.x0]
        y = [self.y0, self.y0 + self.h, self.y0 + self.h, self.y0, self.y0] 

        return (x, y)
    
    @property
    def area(self):
        return self.w * self.h


class Circle(Figure):
    def __init__(self, r=5, x_0=0, y_0=0) -> None:
        super().__init__()
        self.r = r
        # кординаты центра окружности (по умолчанию (0, 0))
        self.x_0 = x_0
        self.y_0 = y_0

        self.parameters = [f"Radius:{self.r}"]


    def getCenter(self) -> tuple[float, float]:
        """Возвращает центр круга"""
        return (self.x_0, self.y_0)

    def getFunc(self) -> tuple[list[float], list[float]]:
        """Возвращает функцию в параметризованном виде"""
        START = 0
        END = 2*np.pi
        N = 1000
        R = self.r
        
        alpha = np.linspace(START, END, N)

        x = self.x_0 + R * np.cos(alpha)
        y = self.y_0 + R * np.sin(alpha)

        return (x, y)

    @property
    def area(self) -> float:
        PI = np.pi
        R = self.r
        area = PI * (R)**2

        return area



class Triangle(Figure):
    def __init__(self, points=[(0, 0), (4, 0), (0, 3)]):
        super().__init__()
        self.points : list[tuple] = points # координаты вершин
        self.parameters = [f"Points: {self.points}"]
        limit_reach = len(self.points) != 3

        if limit_reach:
            raise ValueError(
                f"Ожидается 3 вершины, вы указали {len(self.points)}"
                )

    
    def getCenter(self) -> tuple[float, float]:
        """
        Считает центроид по среднему арифметическому
        """
        x_center = sum(p[0] for p in self.points) / 3
        y_center = sum(p[1] for p in self.points) / 3
        return (x_center, y_center)

    def getFunc(self) -> tuple[list[float], list[float]]:
        x = [self.points[0][0], self.points[1][0], self.points[2][0], self.points[0][0]]
        y = [self.points[0][1], self.points[1][1], self.points[2][1], self.points[0][1]]

        return (x, y)

    @property
    def area(self) -> float:
        # Формула Гаусса (площадь многоугольника по координатам)
        (x1, y1), (x2, y2), (x3, y3) = self.points
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

