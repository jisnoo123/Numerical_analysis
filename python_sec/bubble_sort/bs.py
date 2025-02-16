#Sort numbers using bubble sort
num=list()
n=int(input('No. of elements:'))
for i in range(n):
    num.append(int(input('Enter number:')))

for i in range(n):
    for j in range(n-i-1):
        if num[j]>num[j+1]:
            t=num[j]
            num[j]=num[j+1]
            num[j+1]=t

print(num)