def maximumMinimum(*numbers):
    if not numbers:
        return None
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    return [min_num, max_num]

# Example usage:
input_numbers = input("Enter numbers separated by spaces: ")
numbers = map(int, input_numbers.split())
result = maximumMinimum(*numbers)
print(f"The minimum and maximum numbers are: {result}")
