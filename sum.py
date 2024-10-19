def calculate_sum(numbers):
    total = sum(numbers)
    return total
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
result = calculate_sum(numbers)
print("The sum of the numbers is:", result)
