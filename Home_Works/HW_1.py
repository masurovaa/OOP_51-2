# Задание: Создание класса Hero

class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP


    def introduce(self):
        return (f"Привет, меня зовут {self.name}, мой уровень {self.lvl}, мое HP {self.HP}")


    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False


hero = Hero("Baatyr", 10, 100)
print(hero.introduce())

# Создаем экземпляры героев
hero1 = Hero("Baha", 8, 90)
hero2 = Hero("Toha", 10, 100)
hero3 = Hero("Muha", 15, 70)

# Проверяем каждого героя
print(hero1.is_adult())  # У Baha уровень ниже 10.
print(hero2.is_adult())  # У Toha уровень выше 10.
print(hero3.is_adult())  # У Muha уровень выше 10.




