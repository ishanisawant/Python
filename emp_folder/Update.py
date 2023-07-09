def Updateing():
    try:
        NewID: input("enter new id: ")
        with open("emps.txt", "+r") as u:
            emp = u.readlines()
            flag = False

            for i, employee in enumerate(emp):
                name, id = employee.strip().split("-")
                if id == NewID:
                    flag = True

                    print("\nSelected guy to replace/update is: \n")
                    print(f"name: {name}, id: {id}")

                    newName = input("enter new name: ")
                    newId = input("enter new id: ")

                    if newName:
                        emp[i] = f"{newName}-{newId}\n"
                    else:
                        emp[i] = f"{name}-{id}\n"

                    u.seek(0)
                    u.writelines(emp)
                    u.truncate()

                    print("Update for ", newName, " with id ", newId)
                    break

            if not flag:
                print("Error in updating")
    except Exception:
        print("error")
