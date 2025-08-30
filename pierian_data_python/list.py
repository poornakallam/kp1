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
st="Print only the words that start with s in this sentence"
for word in st.split():
    print(word)

list02=range(0,11,2)
print(list02)

#list03=[num%3 for num in range(1,50,3)]
#print(list03)

myword="Print every word in this sentence that has an even number of letters"
length=len(myword)
if length%2==0:
    print("even")