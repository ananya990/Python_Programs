my_list = [13, 85, 54, 39, 100, 335, 221,]

result = list(filter(lambda x: (x % 5 == 0), my_list))

print("Numbers divisible by 5 are",result)
