def vol(redies):
    return 4/3*22/7*redies
results=vol(21)
print(results)

def ran_check(num,low,high):
    #print(f'{num} in the range between {low} and {high}')
    if num > low and num < high:
        print(True)
    else:
        print(False)     
ran_check(9,1,3)

def up_low(s):
    #s = "Hello Mr. Rogers, how are you this fine Tuesday?"
    for i in s:
        if i == s.upper():
            print(f'upper letter count: {i}')
        elif i == s.lower():
            print(f'lower letter count: {i}')
        else:
            print("nothing")
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

