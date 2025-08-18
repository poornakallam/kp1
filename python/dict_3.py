internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

print(internet_celebrities.update(another_one))
print(internet_celebrities)

insta_cel=internet_celebrities.copy()
# print(internet_celebrities.clear())
# print(internet_celebrities)
# print(insta_cel)
#print(internet_celebrities.setdefault("Discovery", "billionaries"))
internet_celebrities.setdefault("ZLaner", "Instagram")
print(internet_celebrities)
