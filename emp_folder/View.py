def Viewing():
    try:
        with open("emps.txt", "r") as v:
            emps = v.readlines()
            if emps:
                print("\nEmployees in database are as follows: \n")
                for emps in emps:
                    name, id = emps.strip().split("-")
                    print(f"Name: {name}, ID: {id}")
            else:
                print("nothing stored in the database yet")
    except Exception:
        print("error")
