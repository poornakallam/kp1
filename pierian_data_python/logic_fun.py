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
        if word > 3:
            count += 1
    return count
count_words(["hi", "apple", "p", "dog" "banned" ])

