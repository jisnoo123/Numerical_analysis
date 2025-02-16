#Defining the first and second terms of the Fibonacci Sequence
f0=0
f1=1

def fib(n):
    #Returns the nth Fibonacci term
    if n==0:
        return f0
    elif n==1:
        return f1 
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input('Enter n:'))
print('Fibonacci Sequence:')

for i in range(0,n):
    print(fib(i),' ')