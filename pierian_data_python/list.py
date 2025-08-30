mystring=["Hello World"]
mystringint=[1,2,3,4,5,6,7,8,9,10]
mylist=[letter for letter in mystring] # copy from variable

mylist01=[word for word in "hello"] # copy string value

mylist02=[num**2 for num in mystringint]
print(mylist)
print(mylist01)
print(mylist02)

mylist03=[num if num%2==0 else "odd" for num in mystringint]
print(mylist03)

# give empty srting and copy value from one string to another
#mylist.append(letter) - for letter in mystring:

#Assignment

print(range(1,11))
list01=[num%3==0 for num in range(1,50)]
myword="Print every word in this sentence that has an even number of letters"
print(len(myword))

