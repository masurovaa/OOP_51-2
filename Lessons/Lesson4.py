# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора
def my_decorator(func):  # 2

    def wrapper():
        print('Перед выполнением функции')  # 4
        func()  # 5
        print('После выполнением функции')  # 6

    return wrapper  # 3


@my_decorator
def hello():
    print("Привет мир!!")


hello()  # 1

# Декораторы с аргументами
# n = 3
def repeat(n):  # step 2
    # func = greet()
    def decorator(func):  # step 4
        def wrapper(*args, **kwargs):
            for i in range(n):  # step 6
                func(*args, **kwargs)  # step 6

        return wrapper  # step 5

    return decorator


@repeat(3)
def greet():
#    print("Привет!!")


#greet()  # step 1




#def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print('Новый метод!')
    return NewClass

#@class_decorator
#class MyClass:

 #   def old_method(self):
  #      return print("Старый метод!")

#obj = MyClass() #NewClass()
#obj.old_method()
#obj.new_method()



class Person:
    # Магический метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f'бла бла бла')

    obj = Person ('Pavel', 25)

print(obj)




