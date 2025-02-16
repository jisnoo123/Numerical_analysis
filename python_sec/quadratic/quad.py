import math
#To find the roots of a quadratic eqn
print('Quadratic equation of the form: ax^2+bx+c=0')
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
#Discriminant
d=b*b-(4*a*c)

if(d<0):
    r1=(-b+math.sqrt(abs(d)))/(2*a)
    r2=(-b-math.sqrt(abs(d)))/(2*a)
    print("Imaginary roots",r1,'i and',r2,'i')
elif(d>0):
    r1=(-b+math.sqrt(abs(d)))/(2*a)
    r2=(-b-math.sqrt(abs(d)))/(2*a)
    print("Real and distinct roots",r1,' and ',r2)
else:
    r=(-b/(2*a))
    print("Real and equal root(multiplicity:2):",r)