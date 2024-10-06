def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution completed.")

divide_numbers()