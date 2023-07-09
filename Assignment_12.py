from emp_folder.Delete import deleteing
from emp_folder.Add import Adding
from emp_folder.Search import searching
from emp_folder.View import Viewing
from emp_folder.Update import Updateing


while True:
    print("\nEmployee Management Stem")
    print("1. Add Employee")
    print("2. Viw Employee")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Update Employee")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        Adding()
    elif choice == "2":
        Viewing()
    elif choice == "3":
        searching()
    elif choice == "4":
        deleteing()
    elif choice == "5":
        Updateing()
    elif choice == "6":
        print("exiting..............................")
        break
    else:
        print("Invalid")
