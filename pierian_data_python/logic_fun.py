print(20%2 == 0)
def print_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)
        # else:
        #     print(num)
print_even([2,3,4,5,6])

# return statement
def count_words(words):
    count = 0
    for word in words:
        if len(word) > 3:
            count += 1
    return count
result = count_words(["hi", "apple", "p", "dog" "banned" ])
print(result)

#pass condition
def even_numbers(numbers_s):
    even = []
    for numb in numbers_s:
        if numb % 2 == 0:
            even.append(numb)
        else:
            pass
    return even        
results=even_numbers([1,2,3,4,5,6])
print(results)

