class Student:
    def __init__(self, first, last, status):
        self.first = first #These are called instance variables
        self.last = last
        self.status = status
        self.email = first + last + "@mail.weber.edu"

W01234 = Student('Cameron', 'Trejo', 'Pass') # Instance of the student class
W01235 = Student('Waldo', 'Wildcat', 'Pass')

print(W01234.first, W01234.last, W01234.email, W01234.status)
print(W01235.first, W01235.last, W01235.email, W01235.status)

# print(W01234.email)
# print(W01235.email)