class error(Exception):
    pass


class FileOPeraation:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, data):
        with open(self.filename, "w") as file:
            file.write(data)
        return print(f"{data} was inserted into {self.filename}")

    def read_file(self):
        with open(self.filename, "r") as file:
            data = file.read()
        return data

    def append_file(self, data):
        with open(self.filename, "a") as file:
            file.write(data)
        return print(f"{data} appended to {self.filename}")

    def raise_exception(self):
        raise Exception("exception raised")

    def create_file(self):
        try:
            with open(self.filename, "x") as file:
                print(f"{self.filename} created successfully")
        except FileExistsError:
            print(f"{self.filename} is already there")


class String:
    def __init__(self, string):
        self.string = string

    def uniqueCount(self):
        unique_chars = set(self.string)
        return len(unique_chars)

    def upper(self):
        return self.string.upper()

    def lower(self):
        return self.string.lower()

    def reverse(self):
        return self.string[::-1]

    def palin(self):
        self.string = self.string.lower()
        return self.string == self.string[::-1]

    def caps(self):
        return self.string.capitalize()

    def replace(self, old_substr, new_substr):
        return self.string.replace(old_substr, new_substr)

    def split(self):
        return self.string.split()

    def length(self):
        return len(self.string)

    def raise_exception(self):
        raise Exception("exception raised for String Operations")
