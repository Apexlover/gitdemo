#Script Name : fileinfo.py
#Author : LQ
#Created : 2020.03.22
x,y=map(int,input().split())
a,b,c=map(int,input().split())
A=abs(a*x+b*y+c)
B=pow(a**2+b**2,0.5)
D=A/B
D=("%.3f" % D)
print(D)

a11,a12,a13=map(int,input().split())
a21,a22,a23=map(int,input().split())
a31,a32,a33=map(int,input().split())
A=a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a12*a21*a33 - a11*a23*a32
print(A)