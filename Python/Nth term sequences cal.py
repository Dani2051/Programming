#non-linear Nth term calculator

#sequence input
a1 = input('please input the first number of the sequence ')
a2 = input('please input the second number of the sequence ')
a3 = input('please input the third number of the sequence ')
a4 = input('please input the forth number of the sequence ')
a5 = input('please input the fifth number of the sequence ')

#1st common pattern
b1 = int(a2) - int(a1)
b2 = int(a3) - int(a2)
b3 = int(a4) - int(a3)
b4 = int(a5) - int(a4)

#2nd common pattern
c1 = int(b2) - int(b1)

#dividing 2nd common difference by 2
d1 = c1 / 2.0

#Nth term variables
n1 = 1
n2 = 2
n3 = 3
n4 = 4

#putting n**2 variables into equation
n1 = (d1)*(n1**2)
n2 = (d1)*(n2**2)
n3 = (d1)*(n3**2)
n4 = (d1)*(n4**2)

#subtracting inputs by n**2 variables 
a1 = int(a1)-int(n1)
a2 = int(a2)-int(n2)
a3 = int(a3)-int(n3)
a4 = int(a4)-int(n4)

#finding Nth term of new sequence
N1 = int(a2) - int(a1)
N2 = a1 - N1

#printing final Nth term          
if d1 == 1 and N1 == 0 and N2 == 0:
    print(str('n**2'))
    
elif d1 > 1 and N1 == 0 and N2 == 0:
    print(str(d1) + str(' x ') + str('n**2'))
    
elif d1 == 1 and N1 == 1 and N2 == 0:
    print(str('n**2') + str(' + ') + str('n'))
    
elif d1 > 1 and N1 == 1 and N2 == 0:
    print(str(d1) + str(' x ') + str('n**2') + str(' + ') + str('n'))
    
elif d1 == 1 and N1 > 1 and N2 == 0:
    print(str('n**2') + str(' + ') + str(N1) + str('n'))
    
elif d1 > 1 and N1 > 1 and N2 == 0:
    print(str(d1) + str(' x ') + str('n**2') + str(' + ') + str(N1) + str('n'))
    
elif d1 == 1 and N1 == 0 and N2 >= 1:
    print(str('n**2') + str(' + ') + str(N2))
    
elif (d1) > 1 and (N1) == 0 and (N2) >= 1:
    print(str(d1) + str(' x ') + str('n**2') + str(' + ') + str(N2))
    
elif d1 == 1 and N1 == 1 and N2 >= 1:
    print(str('n**2') + str(' + ') + str('n') + str(N2))
    
elif d1 > 1 and N1 == 1 and N2 >= 1:
    print(str(d1) + str(' x ') + str('n**2') + str(' + ') + str('n') + str(' + ') + str(N2))
    
elif d1 == 1 and N1 > 1 and N2 >=1:
    print(str('n**2') + str(' + ') + str(N1) + str('n') + str(' + ') + str(N2))
    
elif d1 > 1 and N1 > 1 and N2 >= 1:
    print(str(d1) + str(' x ') + str('n**2') + str(' + ') + str(N1) + str('n') + str(' + ') + str(N2))
    
else:
    print('there is not mathematical rule with this sequence')
