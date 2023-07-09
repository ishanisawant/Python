def deleteing():
    try:
        gone = input("enter emp id to delete: ")
        with open("emps.txt", "r") as d:
            emp = d.readlines()
        with open("emps.txt", "w") as d:
            flag = False
            for empss in emp:
                id = empss.strip().split("")
                if id != gone:
                    d.write(empss)
                else:
                    flag = True

            if flag:
                print("deleted ", empss, " from database")
            else:
                print("Soemthing went worng couldnt delete ", empss)
    except Exception:
        print("error")
