def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return a * b // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_p = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    return primes

def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result


def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def demonstrate_data_structures():
    print("\n--- Data Structures Demo ---")
    my_list = [1, 2, 3]
    my_list.append(4)
    print("List:", my_list)
    my_tuple = (10, 20, 30)
    print("Tuple:", my_tuple)
    my_set = {1, 2, 2, 3, 3}
    print("Set:", my_set)
    my_dict = {"name": "Student", "course": "CSE"}
    print("Dictionary:", my_dict)


def module1_menu():
    while True:
        print("\n--- MODULE 1: Number Patterns & Sequences ---")
        print("1. Check Armstrong Number")
        print("2. Check Palindrome")
        print("3. Sum of Digits")
        print("4. Fibonacci Sequence")
        print("5. Factorial")
        print("0. Back to Main Menu")
        c = input("Enter choice: ")
        if c == "1":
            n = int(input("Enter a number: "))
            print(n, "is Armstrong:", is_armstrong(n))
        elif c == "2":
            n = int(input("Enter a number: "))
            print(n, "is Palindrome:", is_palindrome(n))
        elif c == "3":
            n = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(n))
        elif c == "4":
            n = int(input("How many terms? "))
            print("Fibonacci:", fibonacci(n))
        elif c == "5":
            n = int(input("Enter a number: "))
            print("Factorial:", factorial(n))
        elif c == "0":
            break
        else:
            print("Invalid choice.")

def module2_menu():
    while True:
        print("\n--- MODULE 2: Number Theory Lab ---")
        print("1. LCM")
        print("2. GCD")
        print("3. Check Perfect Number")
        print("4. Generate Prime Numbers up to N")
        print("5. Power of a Number")
        print("0. Back to Main Menu")
        c = input("Enter choice: ")
        if c == "1":
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("LCM:", lcm(a, b))
        elif c == "2":
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("GCD:", gcd(a, b))
        elif c == "3":
            n = int(input("Enter a number: "))
            print(n, "is Perfect:", is_perfect(n))
        elif c == "4":
            n = int(input("Generate primes up to: "))
            print("Primes:", generate_primes(n))
        elif c == "5":
            base = int(input("Base: "))
            exp = int(input("Exponent: "))
            print("Result:", power(base, exp))
        elif c == "0":
            break
        else:
            print("Invalid choice.")

def module3_menu():
    while True:
        print("\n--- MODULE 3: Matrix & List Operations ---")
        print("1. Matrix Transpose")
        print("2. Linear Search")
        print("3. Bubble Sort")
        print("4. List/Tuple/Set/Dictionary Demo")
        print("0. Back to Main Menu")
        c = input("Enter choice: ")
        if c == "1":
            rows = int(input("Number of rows: "))
            matrix = []
            for i in range(rows):
                row = list(map(int, input(f"Enter row {i+1} values separated by space: ").split()))
                matrix.append(row)
            print("Transposed matrix:", matrix_transpose(matrix))
        elif c == "2":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            target = int(input("Number to search: "))
            result = linear_search(arr, target)
            print("Found at index:", result if result != -1 else "Not found")
        elif c == "3":
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Sorted array:", bubble_sort(arr))
        elif c == "4":
            demonstrate_data_structures()
        elif c == "0":
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n========================================")
        print(" Welcome to NumCraft - Number & Pattern Solver")
        print("========================================")
        print("1. Number Patterns & Sequences")
        print("2. Number Theory Lab")
        print("3. Matrix & List Operations")
        print("0. Exit")
        c = input("Enter choice: ")
        if c == "1":
            module1_menu()
        elif c == "2":
            module2_menu()
        elif c == "3":
            module3_menu()
        elif c == "0":
            print("Thank you for using NumCraft. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()