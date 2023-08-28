#Hex and binary converter

print('Welcome to the Hexadecimal and Binary converter')

hexlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',' ']
binlist = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111','']
        
def main():

    def BinToHex():
        
        convert_text = input('\nPlease input the binary number you want to convert ')
        convert_text = convert_text.strip()
        convert_text_buffer = ''
        
        for a in convert_text:
            if a != '0' and a != '1' and a != ' ':
                print('Input is not in binary format. Please try again...')
                BinToHex()
                
            if a == '0' or a == '1':
                convert_text_buffer  = convert_text_buffer + a
            
            elif a != '0' and a != '1':
                a = ''
                convert_text_buffer  = convert_text_buffer + a
                
        convert_text = convert_text_buffer
        length_text = len(convert_text)
        
        if length_text % 4 == 1:
            convert_text = '000' + convert_text
        elif length_text % 4 == 2:
            convert_text = '00' + convert_text
        elif length_text % 4 == 3:
            convert_text = '0' + convert_text
            
        tick = 1
        nibble = ''
        hex_text = ''
        
        for a in str(convert_text):
            if tick < 4 :
                tick += 1
                nibble = nibble + a 
            elif tick == 4:
                tick = 1
                nibble = nibble + a
                index = binlist.index(nibble)
                nibble = hexlist[index]
                hex_text = hex_text + nibble
                nibble = ''

        print(hex_text)
        again()
        
    def HexToBin():
        
        convert_text = input('\nPlease input the hexadecimal number you want to convert ')
        convert_text = convert_text.strip()
        convert_text = convert_text.upper()
        tick = 1
        bin_text = ''
        
        for a in convert_text:
            if a not in hexlist:
                print('The input you have entered is not hexadecimal. Please try again...')
                HexToBin()
            else:
                index = hexlist.index(a)
                a = binlist[index]
                bin_text = bin_text + a
        
        print(bin_text)
        again()
        
    def again():
        
        again = input('\nDo you want to convert more stuff? (yes/no) ')
        again = again.strip()
        again = again.lower()
        
        if again == 'yes':
            main()
        elif again == 'no':
            print('shutting down...')
        else:
            print('That input is invalid. Please try again...')
            again()

    convert_type = input('\nPlease input what you want to convert to (hex/binary) ')
    convert_type = convert_type.strip()
    convert_type = convert_type.lower()
                
    if convert_type == 'hex':
        BinToHex()
    elif convert_type == 'binary':
        HexToBin()
    else:
        print('That input is not valid. Please try again... ')
        main()

main()
