# vamsi
n=int(input('Enter the value of elements: '))
b=[]
for i in range(n):
    x=int(input())
    b.append(x)
def count_occurrences(numbers):
    occurrences = {}

    # Count occurrences of each number
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    return occurrences

print(count_occurrences(b))