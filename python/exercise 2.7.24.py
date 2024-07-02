str_nums = input()
str_nums = str_nums.split(",")
print(str_nums)
num = [int(str_num) for str_num in str_nums]
print (num)
num = map(int, str_nums)
#print(list(num))
print(set(list(num)))

