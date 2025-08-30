for item in range(1,20,3):
    print(item)

index_count=0
word="abcde"
for letter in word:
    print(word[index_count])
    index_count += 1

#enumerate
for items in enumerate("abcde"):
    print(items)