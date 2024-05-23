# myfile =open('d:\\students.csv','r')

# f=myfile.readlines()
# print(f)

# myfile.close()
f = open('d:\\students.csv')
d=f.readlines()
for line in d:
    avg=sum(int(m.strip()) for m in line.split(',')[2:])/3
    print(avg)
f.close()