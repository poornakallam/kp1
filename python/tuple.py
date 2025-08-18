number=(1,2,3,4,5,6,7,4,5,5,6,6,6,7,8)
print(number[9])
print(number[::3])
#1,4,7,5,6
print(number[2::2])
#3,5,7,5,6,6,8
print(number[3::2])
#4,6,4,5,6,7
print(number[10::-3])
print(number[::-2])
print(number.count(6))
print(number.index(7))

