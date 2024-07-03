print("This program will print all the perfect numbers in a given range")

def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def is_perfect_number(num):
    if num <= 1:
        return False
    return sum_divisors(num) == num

def find_perfect_numbers(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Example usage:
start_range = 1
end_range = 10000
perfect_nums = find_perfect_numbers(start_range, end_range)
print("Perfect numbers between", start_range, "and", end_range, "are:")
print(perfect_nums)
