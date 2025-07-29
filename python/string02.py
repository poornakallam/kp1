name="hello world"

print(name.rjust(15, "-"))
print(name.ljust(15, "-"))
print(name.center(15, "0"))

#parameter=("eggs", "milk", "bread", "milk")

print("eggs, milk, bread, milk".rstrip(", milk"))
print("eggs, milk, bread, milk".rstrip(", bread"))
print("eggs, milk, bread, milk".rstrip(", ilmk"))