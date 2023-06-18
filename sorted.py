# bubble Sort yöntemi
my_list = ['T', 'P', 'A', 'N', 'M', 'G', 'S', 'R', 'V', 'H', 'Q', 'C', 'U', 'Y', 'Z', 'D', 'B', 'K', 'J', 'X', 'O', 'I',
           'W', 'L', 'F', 'E']


def sort_1(my_list):
    for index in range(len(my_list) - 1):
        for index_2 in range(len(my_list) - 1 - index):
            if my_list[index_2] > my_list[index_2 + 1]:
                my_list[index_2], my_list[index_2 + 1] = my_list[index_2 + 1], my_list[index_2]


# sort_1(my_list)
print(my_list)
