'''
#contoh yg bukan user input:
def roman_to_integer(s):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in s:
        value = roman_to_int[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total

def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Example usage
roman_numeral = "MCMXCIV"
integer_value = 1994

print(f"Roman numeral {roman_numeral} is {roman_to_integer(roman_numeral)} as an integer.")
print(f"Integer {integer_value} is {integer_to_roman(integer_value)} as a Roman numeral.")
'''

def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
        
    return total

def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def run_conversion():
    conversion_type = input("Type 'R' to convert a Roman numeral to an integer or 'I' to convert an integer to a Roman numeral: ").strip().upper()

    if conversion_type == 'R':
        roman = input("Enter a Roman numeral: ").strip().upper()
        result = roman_to_integer(roman)
        print(f"The integer value of the Roman numeral {roman} is {result}")
    elif conversion_type == 'I':
        integer = int(input("Enter an integer: "))
        result = integer_to_roman(integer)
        print(f"The Roman numeral representation of the integer {integer} is {result}")
    else:
        print("Invalid choice. Please enter 'R' or 'I'.")

# Run the conversion function directly
run_conversion()
