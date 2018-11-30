class GrumpyDict(dict):
   def __repr__(self):
       print("NONE OF YOUR BUSINESS!")
       return super().__repr__()
       
   def __missing__(self, key):
       print(f"YOU WANT {key}, WELL IT AINT HERE!")
       
   def __setitem__(self, key, value):
       print("YOU WANT TO CHANGE YOUR DICTIONARY!")
       print("OK, FINE THEN!")
       
   def __contains__(self, item):
       print("NO, IT AINT HERE!")
       return False
       
   
   
data = GrumpyDict({"first": "tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
      
