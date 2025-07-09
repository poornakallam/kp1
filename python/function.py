lenght=30
height=20
width=10


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


def rect_lenght(l, w, h):
    return l * w * h

print("the lenght of rectanguler is" + rect_lenght(lenght, width, height) + "feets".)
