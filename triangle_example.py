# Forming a triangle as wide as the number entered from the keyboard. Write a script that justifies left and right.
input_value = input(
    'The program create a trigle with use the chart "*", '
    'if you want create triggle plese input integer value 1-100. If you dont want please write "Y"\n')
lean_value = input(
    'Do you want to lean right or left? (L/R)\n')
character = '*'

if type(int(input_value)) == int:
    if 1 <= int(input_value) <= 100:
        for index in range(0, int(input_value)):
            if lean_value == "L":
                print(character * index)
            elif lean_value == "R":
                print('*' * ((int(input_value) - 1) - index) + character.rjust(1))
            else:
                print("Please write 'L' or 'R' and try again")
    else:
        print("The value not between 0-100")
else:
    print("The value not integer (it's not should be str, list, float etc.)")
