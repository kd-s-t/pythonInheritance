class Head(): 
  
    def eyes(self): 
        return "I have eyes"
  
    def ears(self): 
        return "I have ears"
  
  
# Inherited or Sub class (Note Person in bracket) 
class Body(Head): 
  
    def chest(self): 
        return "I have chest"

    def stomach(self): 
        return "I have stomach"

  
  
parts = Body() # An Object of Employee 
print(parts.chest()) 
print(parts.stomach()) 
print(parts.eyes()) 
print(parts.ears()) 