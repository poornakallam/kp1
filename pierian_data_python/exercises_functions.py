# def animals(a,b):   
#     if a[0] == b[0]:
#         print(True)
#     else:
#         print(False)        
# animals("tiger","turtle")

# def intergers(x,y):
#     if x+y == 20 or x == 20 or y == 20:
#         print(True)
#     else:
#         print(False)        
# intergers(5,25)      

# def myfunc(x,y):
#     if x % 2 == 0 and y % 2 == 0:
#         print(min(x,y))
#     else:
#         print(max(x,y))
# myfunc(6,8)

# Level 01
# def myfunc(name):
#     first_half = name[:3]
#     second_half = name[3:]
#     print(first_half.capitalize() + second_half.capitalize())
# myfunc("macdonald")

# def reverse_func(text):
#     word = text.split()
#     reverse_word = ' '.join(word[::-1])
#     print(reverse_word)
# reverse_func("work with python")

# def number(x):
#     if abs((100 - x) <= 10) or abs((200 - x) <=10):
#         print(True)
#     else:
#         print(False)
# number(50)

#Level 2
def hang_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False                     
result=hang_33([1,3,3,1,3,3])
print(result)

def func(text):
    triple = ''
    for i in text:
        triple += i * 3
        print(triple)
func('hello')        

def intergers(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif sum([a,b,c]) > 21 and 11 in [a,b,c]:
        sum([a,b,c])-10
        return sum([a,b,c])
    else:
        return "BUST"
results=intergers(7,6,5)
print(results)