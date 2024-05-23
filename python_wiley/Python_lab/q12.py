n=input("Enter a sentence : ").split(" ")
b=""
for i in n:
    for j in range(len(i)-1,-1,-1):
        b+=i[j]
    b+=" "
print(b)
