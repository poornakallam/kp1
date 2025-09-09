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

def reverse_func(text):
    word = text.split()
    print(word)
    #reverse_word = ''.join(word[::-1])
reverse_func("work with python")

def number(x):
    if abs((100 - x) <= 10) or abs((200 - x) <=10):
        print(True)
    else:
        print(False)
number(50)



