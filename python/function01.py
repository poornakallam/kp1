celisus=2.112


def farenhit(cel):
    return(cel * 32)/10

print("The farenheat is" + str(farenhit(celisus)) + "degrees.")

    
def round_f(cel):
    return round((cel * 2 + 32), 1)

print(str(round_f(celisus)))


