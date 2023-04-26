# JSON IN PYTHON

import json
import os

# Some Json Data

x = '{"name": "Bolatito", "age": "27", "city": "Lagos"}'

# Convert to Python

y = json.loads(x)
print(y['name'])

# Convert from Python To Json

student = {
    "fname": "Sola",
    "lname": "Asiwaju",
    "age": 35,
    "city": "Ibadan"
}

# Convert to Json

student1 = json.dumps(student)
print(student1)

# File Handling In PYTHON

# file = os.open("C:\Users\USER\Desktop", "x")
# file.write("\nAm Adding to the content of the file")
# file.close()

# file = open("testing.txt", "r")
# print(file.read())

path = r"C:\Users\USER\Desktop"
file_name = "MyFile.txt"

with open(os.path.join(path, file_name), "w") as fp:
    fp.write("NewFile")
