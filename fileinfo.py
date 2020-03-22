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