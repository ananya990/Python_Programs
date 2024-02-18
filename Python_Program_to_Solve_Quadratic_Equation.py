import cmath  #importing complex math module

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are", sol1, "and", sol2)
