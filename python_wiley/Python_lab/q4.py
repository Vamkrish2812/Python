# vamsi
n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
def arr_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if(numbers[j]>numbers[j+1]):
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers

print(arr_sort(b))