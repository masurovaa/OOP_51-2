# Родительский класс


class Heroes:
    def _init_(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} готовится к бою!"

    def attack(self):
        return f"{self.name} атакует врага!"


# Дочерний класс Archer
class Archer(Heroes):
    def _init_(self, name, hp, arrows, precision):
        super()._init_(name, hp)
        self.arrows = arrows
        self.precision = precision  # Значение от 0 до 1 (например, 0.7 — 70% точность)

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:  # Условная вероятность попадания
                return f"{self.name} выпустил стрелу! Попадание!"
            else:
                return f"{self.name} выпустил стрелу, но промахнулся!"
        else:
            return f"{self.name} попытался выстрелить, но у него нет стрел!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} отдохнул и пополнил запас стрел (+5 стрел)."

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision * 100}%"


# Создание экземпляра и вызов методов
if _name_ == "_main_":
    archer = Archer("Леголас", 100, 3, 0.8)

    print(archer.action())  # Леголас готовится к бою!
    print(archer.status())  # Статус персонажа

    print(archer.attack())  # Атака с расходом стрел
    print(archer.attack())  # Еще одна атака
    print(archer.status())  # Проверка статуса после атак

    print(archer.rest())  # Пополнение стрел
    print(archer.status())  # Проверка статуса после отдыха

import random  # Добавляем модуль для случайных значений


# Родительский класс
class Heroes:
    def _init_(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} готовится к бою!"

    def attack(self):
        return f"{self.name} атакует врага!"


# Дочерний класс Archer
class Archer(Heroes):
    def _init_(self, name, hp, arrows, precision):
        super()._init_(name, hp)
        self.arrows = arrows
        self.precision = precision  # Значение от 0 до 1 (например, 0.7 — 70% точность)

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if random.random() <= self.precision:  # Теперь атака зависит от случайного значения
                return f"{self.name} выпустил стрелу! Попадание!"
            else:
                return f"{self.name} выпустил стрелу, но промахнулся!"
        else:
            return f"{self.name} попытался выстрелить, но у него нет стрел!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} отдохнул и пополнил запас стрел (+5 стрел)."

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision * 100}%"


# Создание экземпляра и вызов методов
if _name_ == "_main_":
    archer = Archer("Леголас", 100, 3, 0.8)

    print(archer.action())  # Леголас готовится к бою!
    print(archer.status())  # Статус персонажа

    print(archer.attack())  # Атака с расходом стрел
    print(archer.attack())  # Еще одна атака
    print(archer.status())  # Проверка статуса после атак

    print(archer.rest())  # Пополнение стрел
    print(archer.status())  # Проверка статуса после отдыха