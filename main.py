from students import Student

def main():

    W01234 = Student('Cameron', 'Trejo') # Instance of the student class
    W01235 = Student('Waldo', 'Wildcat')

    # print('Passing Grade :', W01234.passingGrade, W01234.first)
    # print('Passing Grade :', W01235.passingGrade, W01235.first)

    # Student.setPassingGrade(65)

    # print('Passing Grade :', W01234.passingGrade, W01234.first)
    # print('Passing Grade :', W01235.passingGrade, W01235.first)

    print('---------------------')
    print('Start of the Semester')
    print('---------------------')
    W01234.printStudentInfo()
    W01235.printStudentInfo()

    print('----------------------')
    print('Middle of the Semester')
    print('----------------------')

    W01234.setGrade(45)
    W01235.setGrade(75)

    W01234.printStudentInfo()
    W01235.printStudentInfo()

    print('-------------------')
    print('End of the Semester')
    print('-------------------')

    W01234.extraCredit(30)

    W01234.printStudentInfo()
    W01235.printStudentInfo()

if __name__ == "__main__":
    main()