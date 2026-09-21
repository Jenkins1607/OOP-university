"""Отобразить на графике фигуры класса Figure 
+ отобразить и найти координаты центров

Инструменты: matplotlib, matplotlib.patches, 
matplotlib.patches.Polygon
"""
import numpy as np
from typing import Self
from figures import (
    Figure
    )
import matplotlib.pyplot as plt


class FigurePlotter():
    def __init__(self, objects: list[Figure], operation_points: np.ndarray=None):
        # принимаем объекты      
        self.objects = objects
        self.operation_points = operation_points
        self.LEN_OBJECTS = len(self.objects)
        # параметры отображения осей
        self.X_MAX = None
        self.X_MIN = None
        self.Y_MAX = None
        self.Y_MIN = None
        self.EQUAL = 'equal' # одинаковость осей пиксель к пикселю
        # параметры отображения фигур 
        self.LINEWIDTH = 1
        self.ZORDER = 3 # порядок отображения
        # задаем цвета для фигур на графике
        self.COLOR_RED = 'red'
        self.COLOR_GREEN = 'green'
        self.COLOR_BLUE = 'blue'
        
        self.colors = [
            self.COLOR_RED,
            self.COLOR_GREEN,
            self.COLOR_BLUE
            ]

        # data[0] = (x, y) - массив кортежа xy
        # data[1] - массив кортежа (x0, y0) 
        self.data: tuple[list[tuple], list[tuple]] = tuple()

        
    def calculateCoords(self) -> Self:
        """
        Возвращает массивы 
        x,y осей координаты центра
        """
        center_coords = []
        xy_coords = []

        for obj in self.objects: 
            coords: tuple = obj.getFunc()
            center: tuple = obj.getCenter()
            # print(f"{obj.name}: {coords}")
            center_coords.append(center)
            xy_coords.append(coords)

        self.data = (
            xy_coords, 
            center_coords
            )

        return self


    def plotFigures(self) -> Self:
        """
        Отображает фигуры 
        и их центры на плоскости 
        """
        xy_coords = self.data[0] # (x, y) выбирает x
        
        center_coords = self.data[1]
     
        plt.figure(figsize=(10, 5))

        all_x =np.array([])
        all_y = np.array([])
        for i in range(self.LEN_OBJECTS):
            all_x = np.concatenate((all_x, xy_coords[i][0]))
            all_y = np.concatenate((all_y, xy_coords[i][1]))

        
        self.X_MIN, self.X_MAX = min(all_x), max(all_x)
        self.Y_MIN, self.Y_MAX = min(all_y), max(all_y)

        # настройка осей 
        ax = plt.gca()
        ax.set_aspect(self.EQUAL)
        ax.set_xlim(self.X_MIN - 3, self.X_MAX + 3)
        ax.set_ylim(self.Y_MIN - 3, self.Y_MAX + 3)
        
        for i in range(self.LEN_OBJECTS):
            plt.plot(
                xy_coords[i][0], 
                xy_coords[i][1], 
                color=self.colors[i],
                linewidth=self.LINEWIDTH, 
                label=f"{self.objects[i].name}"
            )
            plt.scatter(
                center_coords[i][0], 
                center_coords[i][1], 
                color=self.colors[i], 
                zorder=self.ZORDER,
                s=10
            )  

        # отрисовка точек
        if self.operation_points is not None and len(self.operation_points) > 0:
            plt.scatter(
                self.operation_points[:, 0], # Все X координаты
                self.operation_points[:, 1], # Все Y координаты
                color='purple',              
                s=5,                        # Размер точек 
                zorder=self.ZORDER - 1,      
                label='Operation Points'
            )

        plt.legend(
        loc='lower center',       
        bbox_to_anchor=(0.5, 1.02),  
        ncol=3                      
)
        plt.grid()                        
        plt.tight_layout()
        plt.show()

