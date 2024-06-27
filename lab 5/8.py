def number_to_words(n):
    if n == 0:
        return "zero"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million"]

    def get_hundreds(n):
        hundred = n // 100
        rest = n % 100
        if hundred and rest:
            return units[hundred] + " hundred " + get_tens(rest)
        elif hundred:
            return units[hundred] + " hundred"
        else:
            return get_tens(rest)

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
print(number_to_words(number))  # Output: "one hundred twenty-three"
