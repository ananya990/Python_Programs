def isfloat(num):
    try:
        float(num)
        return True
      
    except ValueError:
        return False

print(isfloat("ch456"))
print(isfloat("12.24"))
