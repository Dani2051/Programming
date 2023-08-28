import sys 

global a
global message
global key
global alphabet
global encrypt1
global decrypt1

def cipher():
    
    key = 0 
    a = input('Do you want to encrypt, decrypt or brute force a message? (0/1/2) ')
   
    alphabet = ('abcdefghiklmnopqrstuvwxyz')
#########################BRUTE############################
    def brute():
        
        brute1 = ''
        brute2 = ''
        key = 1
        while key < 25:
            brute1 = ''
            for i in message:
                position = alphabet.find(i) 
                newposition = (int(position) - int(key))%25
                brute1 += alphabet[newposition]
            print(brute1)    
            key += 1
        if key == 25:
            end = input('Would you like do enter another message? (yes/no) ')
        if end == 'yes':
            cipher()
        else:
            sys.exit() 

##########################################################
    if a == '0' or a == '1':    
        message = input('And what message would you like to ' + a + '? ')
        key = input('what key do you want to use? ')
        
    elif a == '2':
        message = input('And what message would you like to brute force? ')
        brute()
        
    else:
        print('Please select a valid option...')
        cipher()
         
        
    def encrypt():
        
        encrypt1 = '' 
        for i in message:
            position = alphabet.find(i)
            newposition = (int(position) + int(key))%26
            encrypt1 += alphabet[newposition]
        print(encrypt1)
        end = input('Would you like do enter another message? (yes/no) ')
        if end == 'yes':
            cipher()
        else:
            sys.exit()
            
    def decrypt():

        decrypt1 = ''
        for i in message:
            posit = alphabet.find(i)
            newposit = (int(posit) - int(key))%26
            decrypt1 += alphabet[newposit]
        print(decrypt1)
        
        end = input('Would you like do enter another message? (yes/no) ')
        if end == 'yes':
            cipher()
        else:
            sys.exit() 

    if a == 'encrypt':
        encrypt()    
    elif a == 'decrypt':
        decrypt()
cipher()
