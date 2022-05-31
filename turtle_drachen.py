from turtle import *


def drachen(l,n) :
    if n==0 :
        forward(l)
        return
    else :
        l=l/2
        drachen(l,n-1)
        if n%4==1 or n%4==2:
            left(90)
        else :
            right(90)
        drachen(l,n-1)
        
    
 
speed(0)
for i in [0,1,2,3,4] :    
    penup()
    goto(-300,400-i*155)
    write('n='+str(i), True, align="center") 
    pendown()
    drachen(512,i)