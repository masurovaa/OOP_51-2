# Часть 1: Декоратор logger

def logger(func):
    def wrapper(*args, ):
        print(f"Вызов функции: {func.__name__} с аргументами: {args}")
        return func(*args, )  # Возвращаем результат функции

    return wrapper


@logger
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")


# Часть 2: Магические методы в классе Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented


rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 5)

rect3 = rect1 + rect2

print(rect1)
print(rect2)
print(rect3)