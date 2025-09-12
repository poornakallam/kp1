# lambda function is lambda argument: expresion
def square(x):
    return lambda x: x+5
result=square(10)
print(result)
#square([5,10])

# map map() and filter filter()

def numbers(a):
     return filter(lambda x: x>10, map(lambda x: x * 5,a))
results=numbers([2,3,4,5,6,7])
print(list(results))

