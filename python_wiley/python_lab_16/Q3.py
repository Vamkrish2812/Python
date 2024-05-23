n=input("Enter the string: ")
s=""
for i in n:
    if i in 'abcdedefghijklmnopqrstuvwxyz':
        s+=i.upper()
    elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        s+=i.lower()
    else:
        s+=""
print(s)
        