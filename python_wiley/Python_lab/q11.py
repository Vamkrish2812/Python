# vamsi
n=input("Enter the string : ")
c=input("Enter character ")
count=0
for i in n:
    if(i==c):
        count+=1
print(f'The occurence of char {c} in {n} is {count}')