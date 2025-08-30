mystring=["Hello World"]
mystringint=[1,2,3,4,5,6,7,8,9,10]
mylist=[letter for letter in mystring] # copy from variable

mylist01=[word for word in "hello"] # copy string value

mylist02=[num**2 for num in mystringint]
print(mylist)
print(mylist01)
print(mylist02)

mylist03=[if num%2 else "odd" for num in mystringint]

# give empty srting and copy value from one string to another
#mylist.append(letter) - for letter in mystring: