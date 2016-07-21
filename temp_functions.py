def get_input():
    while True:
        try:
            low = int(input("Low range: "))
        except ValueError:
            print("Low value must be a number. ")
        else:
            break
    while True:
        try:
            high = int(input("High range: "))
        except ValueError:
            print("High value must be a number. ")
        else:
            break
    return low, high

def main():
    low, high = get_input()
    print_table(low, high)

def print_table(minimum, maximum):
    print(format("C", ">5s"), format("F", ">8s"))
    print(format("", "=>5s"), format("", "=>8s"))
    for temp_c in range(minimum, maximum+1):
        print_1_row(temp_c)

def print_1_row(temp_c):
    temp_f = 9/5 * temp_c + 32
    print(format(temp_c, '5d'), format(temp_f, '8.1f'))

main()
