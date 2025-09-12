name = "first time" #Global

def parameter():
    name = "second time" #Enclosing 
    def params():
        name = "third time" #Local
        print("Hello " + name)
    params()    
    print("Hello " + name)
parameter()

print(params)
print(parameter)
print(name)