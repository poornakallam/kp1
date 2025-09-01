#Assignment
#01
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
#02    
print(list(range(0,11,2)))
#03
numbers=range(1,51)
for items in numbers:
    if items%3 == 0:
        print(items)
[x for x in range(1,51) if x%3 == 0]        
#04
myword="Print every word in this sentence that has an even number of letters"
# if len(myword)%2==0:
#     print("even")
for word in myword.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")    

#05
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

#06
words = 'Create a list of the first letters of every word in this string'
[word[0] for word in words.split()]

