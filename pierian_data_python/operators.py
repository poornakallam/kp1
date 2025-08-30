# for item in range(1,20,3):
#     print(item)

index_count=0
word="abcde"
for letter in word:
    print(word[index_count])
    index_count += 1

#enumerate
for items in enumerate("abcde"):
    print(items)

mylist1=[1,2,3,4,5]
mylist2=["a","b","c","d"]
for lists in zip(mylist1,mylist2):
    print(lists)
print(min(mylist1))
print(max(mylist1))
print(min(mylist2))