def searching():
    try:
        search = input("enter id tp be searched: ")
        with open("emps.txt", "r") as s:
            empss = s.readlines()
            flag = False

            for emp in empss:
                name, id = emp.strip().split("-")
                if id == search:
                    print("\nEmployee is: \n")
                    print(f"name: {name}, id: {id}")
                    flag = True
                    break
                if not flag:
                    print("Error in finding ", id)
    except Exception:
        print("error")
