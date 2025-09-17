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
    s = "Hello Mr. Rogers, how are you this fine Tuesday?"
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return upper_count, lower_count
print("upper count is:" + upper_count)
print("lower count is:" + lower_count)

