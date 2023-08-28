#Binary convertion calculator


#Loop for if input is greater than 255

def main():
    global Num
    Num = input('Please input a number below 256 ')
    if int(Num) > 255:
        main()
        
main()
    
#Binary placement variables  

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0

#adding '1' to variables if Num >= n 

if int(Num) >= 128:
    a1 = 1
    (Num) = int(Num) - 128
else:
    a1 = 0
if int(Num) >= 64:
    a2 = 1  
    Num = int(Num) - 64
else:
    a2 = 0
if int(Num) >= 32:
    a3 = 1  
    Num = int(Num) - 32
else:
    a3 = 0
if int(Num) >= 16:
    a4 = 1
    Num = int(Num) - 16
else:
    a4 = 0
if int(Num) >= 8:
    a5 = 1
    Num = int(Num) - 8
else:
    a5 = 0
if int(Num) >= 4:
    a6 = 1    
    Num = int(Num) - 4
else:
    a6 = 0
if int(Num) >= 2:
    a7 = 1
    Num = int(Num) - 2 
else:
    a7 = 0
if int(Num) >= 1:
    a8 = 1
else:
    a8 = 0
#printing final binary value

print (str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7) + str(a8))

