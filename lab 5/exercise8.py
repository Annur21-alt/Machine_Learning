#Problem 8 Number to Words:
#Write a program that converts a number to its word representation (e.g., 123 to "one hundred twenty-three").
    

print ("This program will convert a number (123) to its word representation.")
def NumberToWords(n):
    if n == 0:
        return "zero"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million"]

    def get_hundreds(n):
        hundred = n // 100
        remainder = n % 100
        if hundred and remainder:
            return units[hundred] + " hundred " + get_tens(remainder)
        elif hundred:
            return units[hundred] + " hundred"
        else:
            return get_tens(remainder)

    def get_tens(n):
        if n < 10:
            return units[n]
        elif 10 < n < 20:
            return teens[n - 10]
        else:
            ten = n // 10
            unit = n % 10
            return tens[ten] + ("-" + units[unit] if unit else "")

    def get_words(n):
        parts = []
        for thousand in thousands:
            part = n % 1000
            if part:
                parts.append(get_hundreds(part) + " " + thousand if thousand else get_hundreds(part))
            n //= 1000
        return ', '.join(parts[::-1]).strip()

    return get_words(n)

# Example usage
number = 123
print(NumberToWords(number))  # Output: "one hundred twenty-three"
