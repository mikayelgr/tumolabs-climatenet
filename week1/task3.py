# Task 3. A simple calculator program that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. The user selects an operation from a menu, inputs two numbers, and the program outputs the result of the chosen operation. If the user selects 5, the program exits. It includes error handling to manage invalid inputs and prevents division by zero.

def in_number() -> int:
    try:
        """
        Given a prompt returns a parsed integer from the stdin
        """
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid number. Halting the program...")
        exit()

print("------ Welcome to Calculator ------")

while True:
    print("Menu of available options:")
    print("\t1. op_Add")
    print("\t2. op_Sub")
    print("\t3. op_Mul")
    print("\t4. op_Div")
    print("\t5. Exit")
    print("*" * 25)

    n = in_number();
    if n == 5:
        print("Exiting...")
        break

    print("-" * 10)
    print("Provide the inputs:")
    # Getting the numbers in this scope to avoid repeating calls
    # to the in_number function.
    a = in_number()
    b = in_number()
    if n == 1:
        print(f"a + b = {a + b}")
    elif n == 2:
        print(f"a - b = {a - b}")
    elif n == 3:
        print(f"a * b = {a * b}")
    else:
        if b == 0:
            print("Cannot divide by zero. Skipping")
            continue

        print(f"a / b = {a / b}")

