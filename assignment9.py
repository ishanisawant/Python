from Assignment_9_file import FileOPeraation, String

a = 1

file_op = FileOPeraation("meow.txt")
file_op.create_file()
file_op.write_file("helllloooo")
print(f"data: {file_op.read_file()}")
file_op.append_file("byee")


print()


str = input("enter string: ")
string_op = String(str)
if string_op.palin() == True:
    print("is palindrome")
else:
    print("not palindrome")


print(f"unique characters: {string_op.uniqueCount()}")

print(f"lowercase: {string_op.lower()}")

print(f"uppercase: {string_op.upper()}")

print(f"length is: {string_op.length()}")

print(f"caps: {string_op.caps()}")


print(f"splitted: {string_op.split()}")


print(f"reversed string: {string_op.reverse()}")

oldString = input("enter substring: ")
newString = input(f"enter a new substring: ")
replaced = string_op.replace(oldString, newString)


print()


# try block

try:
    string_op.raise_exception()
except Exception as e:
    print(e)
