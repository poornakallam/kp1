def animals(a,b):
    for animal in animals:    
        if animal(a[0]) == animal(b[0]):
            print(True)
        else:
            print(False)
animals("tiger","turtle")

