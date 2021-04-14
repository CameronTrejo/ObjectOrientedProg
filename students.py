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
        print('\nFull name:', self.first, self.last, '\nEmail:', self.email, '\nGrade:', self.grade, '\nAward Credit:', self.awardCredit, '\n')
    
    def passingClass(self):
        if self.grade < self.passingGrade:
            self.awardCredit = False
        else:
            self.awardCredit = True
    
    def setGrade(self, grade):
        self.grade = grade
        self.passingClass()
       
    def extraCredit(self, points):
        self.grade = self.grade + points
        self.passingClass()

    @classmethod
    def setPassingGrade(cls, grade):
        cls.passingGrade = grade
