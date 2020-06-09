#This Script To Create a Very strength Password
import random
import time
import qrcode


mix_c = "AB1CDEFGHI2JKLMN7OP3QRS4TUV8WX5YZ#@*+6-_&!0?%9;/[\]^`{|}~"
lower_mix_c = mix_c.lower()
all_c = mix_c + lower_mix_c
agian = "Y"

while agian == "Y":
    list_1 = []
    
    try:
        Len_pass = int(input('\n[+]Enter how length of the password you want : '))
        if type(Len_pass) == int:
            while len(list_1) < Len_pass:
    
                i = random.choice(all_c)
                list_1.insert(0,i)
    
                if len(list_1)>= Len_pass:
                    strength_password = ''.join(list_1)
                    print('[-]Loading', end='')
                    for i in '...':
                        print(i,end='')
                        time.sleep(1)
                    
                    print(f"\n[-]Your Password With {Len_pass} Character : {strength_password}\n")
                    print('#' * 60)
                    #This part for create a QR Code for your password to save it as image 
                    if input('Do you want QR Code for your Password  [Y/N] : ').capitalize() != 'Y':
                        continue
                    else:
                        king=qrcode.make(f'Your Password is : \n{strength_password}')
                        king.save(input('Entre Name for Photo QR Code : ')+'.png')
                        print("it's Done ")
                    ###############
                    
    

       
    except ValueError:
    
        print('#' * 60)
        print('[-] Please Enter a Digit Number!')
        print('#' * 60)
    finally:
        agian = input('\n[+]Do You New Password ?  [Y/N] ? : ').capitalize()
        if agian != "Y":
            print('Good bye!')
            break
            

input('\nEntre To exit')
