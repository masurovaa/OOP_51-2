# O(1) — Константное время
# Алгоритм работает за фиксированное время,
# независимо от размера входных данных.

# Доступ к элементу списка по индексу — O(1)
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def get_element_by_index(lst, index):
    return lst[index]


# print(get_element_by_index(lst=lst, index=4))


# O(log n) — Логарифмическое время
# Часто встречается в алгоритмах, использующих
# деление входных данных на части (например, бинарный поиск).
lst2 = [9, 2, 21, 6, 83, 1, 8, 0, 21, 3, 5, 7]


def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# print(binary_search(lst, 2))

# O(n) — Линейное время
# Алгоритм проходит по всем входным данным один раз.

def find_element(lst, target):
    for i in lst:
        print(i)
        if i == target:
            return True

    return False


# print(find_element(lst, 10))

lst3 = [9, 2, 5, 1, 5, 2, 8, 7, 45]


# print(lst3.sort())
# print(lst3)


# O(n²) — Квадратичное время
# Обычно встречается в алгоритмах с двумя вложенными
# циклами, например, в пузырьковой сортировке.

def bubble_sort(lst):
    n = len(lst)
    print("for 1  ", range(n))
    for i in range(n):
        print(i)
        print("for 2--", range(n - i - 1))
        for j in range(n - i - 1):  # 2
            print('for 3 ----  ', j)
            if lst[j] > lst[j + 1]:
                print(f"{lst[j]} ----- {lst[j + 1]}")  # Если текуший элемент больше следуйшего
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(f"lists------{lst}")  # Меняем местами


# bubble_sort(lst=lst3)
# print(lst3)


# Пример 1:

# Ввод: nums = [2,7,11,15], цель = 9
#  Вывод: [0,1]
#  Объяснение: поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].


def two_sum(nums, target):
    num_map = {}
    # {
    #    2: 0
    #    7: 1
    # }
    for i, num in enumerate(nums):
        print(f"{i}---{num}")
        #     18 - 2 = 16
        complemenet = target - num
        if complemenet in num_map:
            return [num_map[complemenet], i]
        num_map[num] = i

    return []


nums = [2, 7, 16, 11]
print(two_sum(nums, 18))


