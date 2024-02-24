def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = "")

dec_num = 96

convertToBinary(dec_num)
print()
