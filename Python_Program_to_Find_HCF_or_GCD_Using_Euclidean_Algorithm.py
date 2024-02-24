def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)

print("The HCF of 300 and 400 is", hcf)
