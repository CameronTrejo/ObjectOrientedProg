class Student:
    def __init__(self, first, last, status):
        self.first = first #These are called instance variables
        self.last = last
        self.status = status
        self.email = first + last + "@mail.weber.edu"
    
    # Behaviour
    def printStudentInfo(self):
        print('Full name:', self.first, self.last, '\nEmail:', self.email, '\nStatus:', self.status)

W01234 = Student('Cameron', 'Trejo', 'Pass') # Instance of the student class
W01235 = Student('Waldo', 'Wildcat', 'Pass')

W01234.printStudentInfo()
W01235.printStudentInfo()