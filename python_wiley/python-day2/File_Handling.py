myfile =open('d:\\c390.txt','r')


# myfile.write('i am four winds blowing \n')
# myfile.write('i am the earth \n')
content=myfile.readlines()
print(content)

myfile.close()
print('file created successfully')
