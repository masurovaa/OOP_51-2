""" Наследование - Инкапсуляция - Полиморфизм - Абстракция """

from abc import ABC, abstractmethod



class Animel(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animel):
    def make_sound(self):
        return print('gav gav')

    def move(self):
        return print('run')

dog = Dog()
dog.make_sound()



class OTPService(ABC):

    def sms_send():
        pass

class NikitaOTP(OTPService):
    def sms_send():
        phone = input('')

class TwilioOTP(OTPService):
    def sms_send():






# Модули (встроенные) - пакеты - фреймворки
# Модули (внешние) - библиотеки



#pip pillow













