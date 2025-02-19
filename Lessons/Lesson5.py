# 0 (1) - Константное время


lst = [1,2,3,4,5,6,7,8,9]
def get_element_by_index(lst, index):
    return lst[index]

print(get_element_by_index(lst=lst, index=4))





def binary_search(lst, target):
    left, right = 0, len(lst) -1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1
print(binary_search(lst=lst, target=9))


# O(n) Линейное время

#def find_element(lst, target):
 #   for i in == target:
  #       print(i)
   #     if i == lst:
    #        return True

    #return False

#print(find_element(lst=lst, target=6))

# O (n2) - Квадратичное время
lst3 = [1,12,32,14,5,16,7,18,9]
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j +1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

bubble_sort (lst=lst3)
print (lst3)













