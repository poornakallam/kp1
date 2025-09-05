employee = [("aaa", 30), ("bbb", 25), ("ccc", 20), ("ddd", 35)]

for name, age in employee:
    if age > 25:
        print(name + " is young")
def process_pairs():
    pairs = [(1,2), (3,4), (5,6), (7,8)]

    for x,y in pairs:
        if x % 2 == 1:
            print(f"{x} is even, y={y}")
process_pairs() # without closing function print not works at 'if' condition

def subject_marks():
    marks = [("moon", (85, 95, 90)), ("sun", (80, 75, 65)), ("star", (70, 65, 50))]
    for x, (a,b,c) in marks:
        avg = (a+b+c)/3
        if a >= 80 and b > 70 and c > 60 and avg >= 40:
            print(f"{x} is above {a}, {b} and {c}")
subject_marks()            


