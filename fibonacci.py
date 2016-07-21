#Fibonacci sequence
def main():
    position = int(input("Enter an index position: "))
    output = fib(position)
    print("Fibonacci number at position", position, "equals", output)
    
def fib(index):
    if index > 1:
        return fib(index-2) + fib(index-1)
    elif index == 1:
        return 1
    elif index == 0:
        return 0
    else:
        return "none"


main()
