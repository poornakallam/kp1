print(20%2 == 0)

# def even_number_list(num_list):
#     return num_list%2 == 0
#     #print(num_list%2 == 0)
# print(even_number_list([1,2,3,4]))
# list and int not working at function variable or argument

def numbers(number):
    for num in number:
        if num % 2 == 0:
            print(True)
        else:
            print(False)
numbers(30)       