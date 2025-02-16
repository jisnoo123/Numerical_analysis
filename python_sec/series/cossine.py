n=int(input('Enter number of terms:'))
cos=0
sin=0
x=float(input('Enter angle(in degrees):'))
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#Cosine and Sine

for i in range(n):
    cos=cos+(((-1)**i)*(x**(2*i))/fact(2*i))
    sin=sin+(((-1)**i)*(x**((2*i)+1))/fact((2*i)+1))

print('sin',x,':',sin,'cos',x,':',cos)