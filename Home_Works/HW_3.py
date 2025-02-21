# Скачать внешний модуль или библиотеку.

# pip install numpy - Installing collected packages: numpy
# Successfully installed numpy-2.2.3


# NumPy (Numerical Python) – это библиотека для работы с многомерными массивами
# и выполнения математических операций. Она является основой для научных
# вычислений в Python и используется во многих других библиотеках, включая pandas,
# scikit-learn, tensorflow и другие.



import numpy as np
arr = np.array([1,2,3,4,5])

arr_multiplied = arr * 2
print(arr ,"это исходные данные")
print(arr_multiplied ,"данные умноженные на 2")