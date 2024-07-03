def sum_of_proper_divisors(n):
    divisors_sum = 1  # 1 is a proper divisor of any number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def amicableNumbers(lower, upper):
    amicable_pairs = []
    for num in range(lower, upper):
        sum1 = sum_of_proper_divisors(num)
        if sum1 > num and sum1 < upper:
            sum2 = sum_of_proper_divisors(sum1)
            if sum2 == num:
                amicable_pairs.append((num, sum1))
    return amicable_pairs

# Example usage:
print(amicableNumbers(1, 1000))
