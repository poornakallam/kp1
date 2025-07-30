user_string = "something123"
reversed = ""
 
for item in range(len(user_string) - 1, -1, -1):
    reversed = user_string[item]
 
print(reversed)