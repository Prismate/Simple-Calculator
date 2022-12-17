def choose_number(str):
    while(True):
        str = input("Choose a number: ")
        try:
            str = float(str)
            return float(str)
        except:
            print("This is not a number")

def choose_operator(str):
    while(True):
        str = input("Choose your operator ('+' or '-' or '*' or '/'): ")
        if str == "+" or str == "-" or str == "*" or str == "/":
            return str
        else:
            print("This is not an operator")

def calculation(a, b, operator):
    if operator == "+":
        print(f"{a} plus {b} equals {a + b}")
    elif operator == "-":
        print(f"{a} minus {b} equals {a - b}")
    elif operator == "*":
        print(f"{a} times {b} equals {a * b}")
    elif operator == "/":
        print(f"{a} divide by {b} equals {a / b}")

def startup_message():
    print("--------------) SIMPLE CALCULATOR (---------------")

def simple_calculator():
    startup_message()
    a = choose_number(str)
    operator = choose_operator(str)
    b = choose_number(str)
    calculation(a, b, operator)


if __name__ == '__main__':
    simple_calculator()


# Simple Calculator by Pryzmate
