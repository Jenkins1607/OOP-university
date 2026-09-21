"""
Написать программу на Python,
которая визуализирует логические операции 
(объединение, пересечение, разность) 
над двумя геометрическими фигурами.
"""


from figures import Figure
from matplotlib.path import Path
import numpy as np


class FigureOperations:
    def __init__(self, objects: list[Figure]):
        self.objects = objects
        self.LEN_OBJECTS = len(self.objects)
        self.RESOLUTION = 200
        self.path1 = None
        self.path2 = None
        self.points = None
        self.in_path1 = None
        self.in_path2 = None


    def toPaths(self):
        """
        Преобразовывает два отдельных массива
        list[x: list[float], y: list[float]]
        к двумерному массиву соответствий (x1,y1), (x2,y2)...
        """
        # x,y координаты obj1
        obj1 = self.objects[0].getFunc()
        # x,y координаты obj2
        obj2 = self.objects[1].getFunc()

        # создаем 2д массивы (N, 2) x, y для каждого из obj(фигуры)
        vertices1 = np.column_stack((obj1[0], obj1[1]))
        vertices2 = np.column_stack((obj2[0], obj2[1]))

        # преобразуем в контур (путь)
        self.path1 = Path(vertices1)
        self.path2 = Path(vertices2)


    def getAxes(self):
        """
        Определяет bounding box для будущей сетки (getGrid)
        """
        obj1 = self.objects[0].getFunc()
        obj2 = self.objects[1].getFunc()

        all_x = np.concatenate((obj1[0], obj2[0]))
        all_y = np.concatenate((obj1[1], obj2[1]))

        X_MIN, X_MAX = min(all_x), max(all_x)
        Y_MIN, Y_MAX = min(all_y), max(all_y)

        x_grid = np.linspace(X_MIN, X_MAX, self.RESOLUTION)
        y_grid = np.linspace(Y_MIN, Y_MAX, self.RESOLUTION)

        return x_grid, y_grid


    def getGrid(self):
        """
        Готовит сетку;
        вычисляет точки контуров,
        пересекающиеся с сеткой 
        """
        x_grid, y_grid = self.getAxes()
        xv, yv = np.meshgrid(x_grid, y_grid)
        self.points = np.column_stack((xv.ravel(), yv.ravel()))

        self.in_path1 = self.path1.contains_points(self.points)
        self.in_path2 = self.path2.contains_points(self.points)


    def prepare(self):
        """
        Готовит объект
        к вызову логических 
        операций
        """
        self.toPaths()
        self.getGrid()


    def intersection(self):
        """Пересечение"""
        mask = self.in_path1 & self.in_path2
        return self.points[mask]


    def union(self):
        "Объединение"
        mask = self.in_path1 | self.in_path2
        return self.points[mask]


    def difference(self):
        """Разность"""
        mask = self.in_path1 & ~self.in_path2
        return self.points[mask]

