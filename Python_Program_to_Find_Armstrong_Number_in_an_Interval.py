lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))

print("The armstrong numbers in the range",lower,"to",upper,"are:")

for num in range(lower, upper + 1):
    order = len(str(num))  
    sum = 0  
    temp = num
  
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

    if num == sum:
       print(num)
