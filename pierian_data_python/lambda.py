# lambda function is lambda argument: expresion
def square(x):
    print(lambda x: x+5)
square(10)
#square([5,10])

# map map() and filter filter()

def numbers(a):
    filter(lambda x: x>10, map(lambda x: x * 5))
results=numbers([2,3,4,5,6,,7])
print(results)

