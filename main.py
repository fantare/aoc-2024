import math

first_list = [3, 4, 2, 1, 3, 3]
second_list = [4, 3, 5, 3, 9, 3]
sum_list = []

def get_distance (x, y):
    x = first_list
    y = second_list
    n = len(x)
    count = 0

    while n > 0:
        sum_list.append(abs(min(x) - min(y)))
        first_list.remove(min(x))
        second_list.remove(min(y))
        n -= 1
    
    for num in sum_list:
        count += num

    return count

print(get_distance(first_list, second_list))