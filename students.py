class Student:
    grade = 0
    passingGrade = 75
    awardCredit = False

    def __init__(self, first, last):
        self.first = first #These are called instance variables
        self.last = last
        self.email = first + last + "@mail.weber.edu"
    
    # Behaviour
    def printStudentInfo(self):
        print('Full name:', self.first, self.last, '\nEmail:', self.email, '\nGrade:', self.grade, '\nAward Credit:', self.awardCredit)

    def setGrade(self, grade):
        self.grade = grade
        if self.grade < self.passingGrade:
            self.awardCredit = False
        else:
            self.awardCredit = True

W01234 = Student('Cameron', 'Trejo') # Instance of the student class
W01235 = Student('Waldo', 'Wildcat')

print('Start of the Semester')
print('---------------------')
W01234.printStudentInfo()
W01235.printStudentInfo()

print('Middle of the Semester')
print('---------------------')

W01234.setGrade(45)
W01235.setGrade(75)

W01234.printStudentInfo()
W01235.printStudentInfo()

print('End of the Semester')
print('---------------------')
W01234.printStudentInfo()
W01235.printStudentInfo()