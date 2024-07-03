import time

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    reversed_n = int(str(n)[::-1])
    result = n + reversed_n
    return result, reversed_n

def find_lychrel_palindrome(starting_number):
    count = 0
    current_number = starting_number

    while not is_palindrome(current_number):
        reversed_n = int(str(current_number)[::-1])
        result = current_number + reversed_n
        print(f"Iteration {count}: {current_number} + {reversed_n} = {result}")
        current_number = result
        count += 1
        time.sleep(1)

    print(f"Palindrome found: {current_number} after {count} iterations")

if __name__ == "__main__":
    starting_number = int(input("Enter a number: "))
    find_lychrel_palindrome(starting_number)

