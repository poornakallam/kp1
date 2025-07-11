key="value"
fruit="banana"

def loc_ex():
    name="local value"
    return name

print(loc_ex())

def loc_exe():
    code= "code"
    print(key  + code)

loc_exe()

def glo_ex():
    return key

print(glo_ex())

def loc_exec():
    global fruit
    fruit="apple"
    print(fruit)

loc_exec()
print(fruit)
