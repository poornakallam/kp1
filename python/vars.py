key="value"

def loc_ex():
    name="local value"
    return name

print(loc_ex())

def loc_exe():
    code="code"
    print(key  + code)

loc_exe()

def glo_ex():
    return key

print(glo_ex())