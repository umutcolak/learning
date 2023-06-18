import random

my_list = [24, 5, 12, 3, 26, 9, 14, 27, 8, 17, 7, 19, 30, 4, 1, 25, 10, 11, 23, 15, 18, 20, 13, 16, 28, 21, 2, 29, 6,
           22]


def get_second_value():
    second = my_list[random.randint(0, len(my_list))]
    first = my_list[random.randint(0, len(my_list))]
    for index in range(len(my_list) - 1):
        if my_list[index] > (my_list[index + 1] and first):
            first = my_list[index]
        elif my_list[index] < (my_list[index + 1] and second):
            second = my_list[index]
    print(str(first) + "  " + str(second))


get_second_value()
