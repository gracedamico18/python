#draw a triangle with **** out of a recursion method

def main():
    n = int(input("Enter an integer: "))
    triangle(n)

def triangle(num):
    if num >= 1:
        print("*" * num)
        num -= 1
        triangle(num)

main()
