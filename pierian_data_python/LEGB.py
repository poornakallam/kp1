name = "first time" #Global

def parameter():
    name = "second time" #Enclosing 
    def params():
        name = "third time" #Local
        print("Hello " + name)
    params()  
    print("Hello " + name)
parameter()

print(name)

number = 20
def change():
    global = number
    number = 10
    print(f"number is overridden by local var {number}")
change()    
print(number)