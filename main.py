from figures import Rectangle, Circle, Triangle
from operations import FigureOperations
from centers import FigurePlotter

def test_centers():
    triangle_points = [
        (0, 0), 
        (4, 0), 
        (0, 3)
        ]
    
    objects=[
        Circle(), 
        Rectangle(), 
        Triangle(triangle_points)
        ]
    
    plotter = FigurePlotter(objects)
    plotter.calculateCoords().plotFigures()


def test_operations():
    # 1. Частичное пересечение

    triangle_points = [
            (0, 0), 
            (4, 0), 
            (0, 3)
            ]
        
    objects=[
            Rectangle(), 
            Triangle(triangle_points)
            ]

    test0 = objects
    test1 = [Circle(r=5, x_0=0, y_0=0), Rectangle(w=10, h=10, x0=3, y0=3)]

    # 2. Одна фигура полностью внутри другой
    test2 =[Circle(r=100), Rectangle(w=20, h=20, x0=-10, y0=-10)]

    # 3. Нет пересечения (разность вернет всю первую фигуру)
    test3 = [Circle(r=3, x_0=-8, y_0=-8), Rectangle(w=5, h=5, x0=2, y0=2)]

    # 4. Касание / сложное наложение
    test4 = [Triangle(points=[(0,0), (10,0), (5,10)]), Circle(r=4, x_0=5, y_0=3)]

    operations = FigureOperations(test0)
    operations.prepare()
    
    result_points = operations.intersection()

    plotter = FigurePlotter(objects=test0, operation_points=result_points)
    plotter.calculateCoords().plotFigures()


def main():
    test_operations()
    # test_centers()
main()

