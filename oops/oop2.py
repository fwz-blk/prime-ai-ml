class student:
    def __init__(self,name,cgpa):
        self.name = name 
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
    
    
stu1 = student("fawaz",6)
stu2 = student("faaiz",5)
stu3 = student("fawzan",9)


print(stu1.name,stu2.cgpa)