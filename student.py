'''making a class Student with attributes student_id, name, age and marks and validating the attributes'''
class Student:
    '''Constructer to initialize the student object with student_id, name, age and marks'''
    def __init__(self,student_id,name,age,marks,):

        '''Set Validations'''
        
        if not isinstance(student_id,int) or isinstance(student_id,bool) or (student_id <= 0):
            raise ValueError ("StudentID must be a positive integer")

        if not isinstance(name,str) or not name.strip():
            raise ValueError("Nmae must not be empty.")

        if not isinstance(age,int)or isinstance(age,bool) or age<=0:
            raise ValueError("Age must be a positive integer")

        if not isinstance(marks,(int,float))or isinstance(marks,bool) or not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")


        ''' Store Validations'''
        self.student_id = student_id
        self.name= name.strip()
        self.age = age
        self.marks = marks       


try:
    age =         int(input("Enter your age: "))
    marks=        float(input("Enter your marks: "))  
    name=         input("Enter your name : ")
    student_id =  int(input("Enter you student_id: ")) 

    student_1 =Student(student_id,name,age,marks)    

    print("\nStudent created successfully!")
    print("Student ID",student_1.student_id)
    print("Student Name",student_1.name)
    print("Student Age",student_1.age)
    print("Student Marks",student_1.marks)


except ValueError as error:
    print("Invalid Input",error)

 