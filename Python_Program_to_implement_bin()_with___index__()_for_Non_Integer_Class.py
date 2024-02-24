class Quantity:
    blue = 1
    yellow = 2
    red = 2
    
    def __index__(self):
        return self.blue + self.yellow + self.red
        
print("The binary equivalent of quantity is :", bin(Quantity()))
