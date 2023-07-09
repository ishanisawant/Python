def Adding():
    try:
        with open("emps.txt", "a") as a:
            name = input("enter emp name: ")
            id = input("enter emp id: ")

            a.write(f"{name}-{id}\n")
            print("updates database")
    except Exception:
        print("error")
