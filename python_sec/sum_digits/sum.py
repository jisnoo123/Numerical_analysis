#Sum of digits of a number
n=int(input('Enter number:'))
s=0
b=n
while(b!=0):
    d=(b%10)
    s=s+d
    b//=10
    
print('Sum of digits:',s)