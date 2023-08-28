#Nth term calculator (non/linear)

#Non-linear sequence function
print('Nth rule calculator! ')

def main():

    #global
    global a1
    global a2
    global a3
    global a4
    global b1
    global b2
    global c1
    global d1
    global n1
    global n2
    global x1
    global x2
    global N1
    global N2
    
    #reset values 
    a1 = None 
    a2 = None
    a3 = None
    a4 = None
    a5 = None
    b1 = None
    b2 = None
    b3 = None
    c1 = None
    d1 = None
    n1 = None
    n2 = None
    n3 = None
    n4 = None
    x1 = None
    x2 = None
    N1 = None
    N2 = None

    #input values    
    print('')
    a1 = int(input('please input the first number of the sequence '))
    a2 = int(input('please input the second number of the sequence '))
    a3 = int(input('please input the third number of the sequence '))
    a4 = int(input('please input the forth number of the sequence '))

    if a1 == '' or a2 == '' or a3 == '' or a4 == '':
        print('Please make sure all inputs are filled with a number... ')
        main()
    
    #Linear Nth term calculator
    def Linear():
        global a1
        global a2
        global a3
        global a4
        global a5
        global b1
        global b2
        global c1
        global d1
        global n1
        global n2
        global x1
        global x2
        global N1
        global N2
        
        c1 = int(b2) - int(b1)
        d1 = int(c1) / 2
        n1 = int(d1)*(1**2)
        n2 = int(d1)*(2**2)
        x1 = int(a1) - int(n1)
        x2 = int(a2) - int(n2)
        N1 = int(x2) - int(x1)
        N2 = int(x1) - int(N1)
      
        #loop back to code
        if int(N1)%1 != 0 and int(N2)%1 != 0:
            print('The sequence is neither arithmetic or geometric. Please try again... ')
            main()
            import sys
            sys.exit() 
        
        elif int(N1) * 1 + N2 != int(a1) or int(N1) * 2 + N2 != int(a2) or int(N1) * 3 + N2 != int(a3) or int(N1) * 4 + N2 != int(a4):
            print('The sequence is neither arithmetic or geometric. Please try again... ') 
            main()
            import sys
            sys.exit()

        elif int(N1) == 0:
            print('The sequence is neither arithmetic or geometric. Please try again...')
            main()
            import sys
            sys.exit() 

        print('')
        
        #outputting final calculations
        Sign = 0
        Sign1 = 0
        
        if int(N1) == 1:
            N1 = ('')
            Sign = ('')

        elif int(N1) == -1:
            Sign = ('-')
            N1 = ('')

        elif int(N1) < 0:
            Sign = ('-')
            N1 = (int(N1) - int(N1) - int(N1))

        if int(N2) >= 1:
            Sign1 = (' + ')
            
        elif int(N2) < 0:
            N2 = (int(N2) - int(N2) - int(N2))
            Sign1 = (' - ')

        elif int(N2) == 0:
            N2 = ('')
            Sign1 = ('')

        print(str(Sign) + str(N1) + str('n') + str(Sign1) + str(N2))
        print('')
        Rst = input('Any more sequences? ')
        if Rst == ('yes'):
            main()
        else:
            import sys
            sys.exit()
                
    #1st common pattern
    b1 = int(a2) - int(a1)
    b2 = int(a3) - int(a2)
    b3 = int(a4) - int(a3)
    
    #2nd common pattern
    c1 = int(b2) - int(b1)
    if c1 == 1:  
        Linear()
        import sys
        sys.exit() 
    elif (b3) - (b2) != c1 or c1 == 0:
        Linear()
        import sys
        sys.exit() 
    #dividing 2nd common difference by 2
    d1 = (c1) / 2
    if (d1)%1 != 0: 
        Linear()
        import sys
        sys.exit() 
    #putting n**2 variables into equation
    n1 = (d1)*(1**2)
    n2 = (d1)*(2**2)
    n3 = (d1)*(3**2)
    n4 = (d1)*(4**2)
    
    #subtracting inputs by n**2 variables 
    x1 = int(a1) - int(n1)
    x2 = int(a2) - int(n2)
          
    #check to see if sequence is Linear or not
    N1 = int(x2) - int(x1)
    N2 = int(x1) - int(N1)
    
    if int(a2) - int(a1) == int(a3) - int(a2) == int(a4) - int(a3):
        Linear()
        import sys
        sys.exit()


    #printing Nth rule

    def cleanup(d1,N1,N2):

        nsquared = 'n^2'
        n = 'n'
        sign1 = ('')
        sign2 = ('')
        sign3 = ('')
        d1 = int(d1)
    
        if d1 == 0: #minus value
            d1 = ''
            nsquared = ''

        elif d1 < 0: #no value
            d1 = d1*-1
            sign1 = ' - '
            
        elif d1 == 1: #value of one
            d1 = ''

        elif d1 == -1: #value of one
            d1 = d1*-1
            sign1 = ' - '

        if N1 == -1: #value of negative one
            sign2 = ' - '
            N1 = ''
            n = 'n'
                        
        elif N1 < 0: #minus value
            sign2 = ' - '
            N1 = N1*-1
            
        elif N1 == 0: #no value
            sign2 = ''
            N1 = ''
            n = ''
            
        elif N1 == 1: #value of one
            sign2 = ' + '
            N1 = ''
            n = 'n'
            
        elif N1 > 1: #positive value
            sign2 = ' + '
            n = 'n'

        if N2 < 0: #minus value
            sign3 = ' - '
            N2 = N2*-1
            
        elif N2 == 0: #no value
            sign3 = ''
            N2 = ''
            
        elif N2 == 1: #value of one
            sign3 = ' + '
            N2 = '1'
            
        elif N2 > 1: #positive value
            sign3 = ' + '

        print('')
        print(str(sign1) + str(d1) + str(nsquared) + str(sign2) + str(N1) + str(n) + str(sign3) + str(N2))
        Rst = input('\nAny more sequences? (yes/no) ')
        if Rst == ('yes'):
            main()
        else:
            import sys
            sys.exit()
            
    cleanup(d1,N1,N2)

    
#Function call    
main()
print('')    
        

