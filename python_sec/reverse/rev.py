#Reverse a number
n=int(input('Enter a numnber:'))
r=0
b=n
while(b!=0):
    r=(r*10)+(b%10)
    b//=10
print('Reverse of',n,'is :',r)