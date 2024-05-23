# # print({f'{x}:{x*x}' for x in range(10)})

# pw=[110,120,130,140,150,160]

# print({f'{x} pounds :{round(x*0.4534)}' for x in pw})

# color=['red', 'orange', 'maroon', 'indigo', 'cyan']

# print({f'{x}:length is {len(x)}' for x in color})

# score=[41,67,32,28,84,76]

# print({x:'fail' if x<44 else 'pass' for x in score})

# getsquare =  lambda num: num*num

# print(getsquare(7))

# getforce= lambda mass ,acc:mass*acc
# print(getforce(2500,9.4))

# pw=[110,120,130,140,150,160]
# lbstokg=lambda lbs:lbs*0.45
# print([lbstokg(x) for x in pw])

# ftoc=lambda f: (f - 32) * 5/9

# print(ftoc(98.6))

#scientists= 'Thomas Edison,Georg Simon Ohm,John Dalton,Pierre Louis Dulong'
# names=lambda x:x+'.'+x[0][0]

# print([f'Dear Mr. {x} . {x[0][0]}' for x in scientists.split(",")])

# b=scientists.split(',')
# d= lambda  s : f'Dear Mr. {s.split('') [-1]} . {s[0].upper()}

n=input()
r=n[::-1]
c=""
ce={'a':'0','e':'1','i':'2','o':'3','u':'4'}
for i in r:
    if i in 'aeiou':
        n=ce[i]
        c+=n
    else:
        c+=i
c=c+'aca'
print(c)
