class Student:
    pass

W01234 = Student()
W01235 = Student()

print(W01234)
print(W01235)

W01234.first = "Cameron"
W01234.last = "Trejo"
W01234.email = "camerontrejo2000@gmail.com"
W01234.status = "Pass"

W01235.first = "Waldo"
W01235.last = "Waldo"
W01235.email = "waldowildcat@weber.edu"
W01235.status = "Pass"

print(W01234.email)
print(W01235.email)