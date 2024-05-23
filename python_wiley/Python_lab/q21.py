# vamsi
c=int(input('Enter the number of students: '))
b=[]
for i in range(c):
    roll_no=int(input('Enter the roll number: '))
    stud_name=input('Enter the name: ')
    mark1=int(input('Enter the mark1: '))
    mark2=int(input('Enter the mark2: '))
    mark3=int(input('Enter the mark3: '))
    total=(mark1+mark2+mark3)
    avg_marks=total//3
    b.append((roll_no,stud_name,mark1,mark2,mark3,total,avg_marks))
sorted_stud = sorted(b, key=lambda x: x[5],reverse=True)
for i in sorted_stud:
    print(i)
