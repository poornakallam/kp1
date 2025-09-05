def get_employee():
    employee = [("aaa", 30), ("bbb", 25), ("ccc", 20), ("ddd", 35)]

    for name, age in get_employee():
        if age > 25:
            print(name + "is young")