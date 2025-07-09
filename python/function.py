length=30
width=10
height=20

def hello():
    print("hello world")

hello()    

def name_printer(p):
    print(p + 2)

name_printer(7)

#def rectanguler(l):
#    return l * b * w
#
#print(rectanguler(20))


def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + (prism_vol(length, width, height) + " cubic feet.")
