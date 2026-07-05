class employe:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get__cgpa(self):
        return self.salary
emp1=employe("Aryan",2000)
emp2=employe("Ansh",2100) 

print(f"Employe {emp1 .name} has get {emp1.salary} ")
print(f"Employe {emp2 .name} has get {emp2.salary} ")