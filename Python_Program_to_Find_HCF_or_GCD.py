def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
      
    for i in range(1, smaller+1):
        # checking if both x and y are divisible by the current iterator i
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
          
    return hcf

num1 = int(input("Enter first number : ")) 
num2 = int(input("Enter second number : "))

print("The H.C.F. of",num1,"and",num2,"is", compute_hcf(num1, num2))
