from figures import Rectangle, Circle, Triangle
from operations import FigureOperations
from plotter import FigurePlotter


def _run_operation_test(objects: list, operation: str, description: str):
    """
    Вспомогательная функция для запуска и отрисовки логической операции.
    """
    print(f"\n▶ Запуск: {description} (Операция: {operation})")
    
    ops = FigureOperations(objects)
    ops.prepare()
    
    if operation == "intersection":
        result_points = ops.intersection()
    elif operation == "union":
        result_points = ops.union()
    elif operation == "difference":
        result_points = ops.difference()
    else:
        raise ValueError(f"Неизвестная операция: {operation}")

    plotter = FigurePlotter(objects=objects, operation_points=result_points)
    plotter.calculateCoords().plotFigures()


# ТЕСТИРУЕМ ОТРИСОВКУ И НАХОЖДЕНИЕ ЦЕНТРОВ ФИГУР
def test_centers_basic():
    """Тест отрисовки фигур и их центров"""
    triangle_points = [(0, 0), (4, 0), (0, 3)]
    objects = [Circle(), Rectangle(), Triangle(triangle_points)]
    
    plotter = FigurePlotter(objects)
    plotter.calculateCoords().plotFigures()


# ТЕСТИРУЕМ ЛОГИЧЕСКИЕ ОПЕРАЦИИ
def test_op_partial_intersection():
    """1. Частичное пересечение"""
    objects = [
        Rectangle(w=100, h=100), 
        Triangle(points=[(0, 0), (40, 0), (0, 300)])
    ]
    _run_operation_test(objects, "intersection", "Частичное пересечение")


def test_op_full_containment():
    """2. Одна фигура полностью внутри другой"""
    objects = [
        Circle(r=100), 
        Rectangle(w=20, h=20, x0=-10, y0=-10)
    ]
    _run_operation_test(objects, "intersection", "Полное вложение (пересечение)")


def test_op_no_intersection():
    """3. Нет пересечения"""
    objects = [
        Circle(r=3, x_0=-8, y_0=-8), 
        Rectangle(w=5, h=5, x0=2, y0=2)
    ]
    _run_operation_test(objects, "union", "Нет пересечения (объединение)")


def test_op_complex_overlap():
    """4. Касание / сложное наложение"""
    objects = [
        Triangle(points=[(0, 0), (10, 0), (5, 10)]), 
        Circle(r=4, x_0=5, y_0=3)
    ]
    _run_operation_test(objects, "intersection", "Сложное наложение (пересечение)")

def test_op_difference():
    """Тест разности: Круг минус Прямоугольник"""
    objects = [
        Circle(r=10, x_0=0, y_0=0), 
        Rectangle(w=8, h=8, x0=2, y0=2)
    ]
    _run_operation_test(objects, "difference", "Разность (Круг - Прямоугольник)")


def tests_run():

    test_centers_basic()
    
    # test_op_partial_intersection()
    # test_op_full_containment()
    # test_op_no_intersection()
    # test_op_complex_overlap()
    # test_op_difference()

if __name__ == "__main__":
    tests_run()