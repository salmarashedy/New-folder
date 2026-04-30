def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

if __name__ == "__main__":
    print("1-Add 2-Subtract 3-Multiply 4-Divide")
    choice = input("Choice: ")

    a = float(input("First: "))
    b = float(input("Second: "))

    if choice == "1":
        print(add(a, b))
    elif choice == "2":
        print(subtract(a, b))
    elif choice == "3":
        print(multiply(a, b))
    elif choice == "4":
        print(divide(a, b))