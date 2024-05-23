# list inside demo can be manupulated
demo=(1,2,[3,4])
f1,f2,f3=demo
print(f1)
print(f2)
print(f3)
demo[2][0]=99
print(demo)