data={
    "satnam":'A',
    "Rahul":'B',
    "Priya":'C'
}

print("enter student name")

name = input()

print("Enter the grade")

grade = input()
data[name]=grade

print("updated student data")
print(data)