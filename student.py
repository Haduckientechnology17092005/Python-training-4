student = []
def inputName(n):
    for i in range(n):
        name = input("Enter name: ")
        print("Hello", name)
        student.append(name)

n = int(input("Enter number of students: "))
inputName(n)
print(student)
        