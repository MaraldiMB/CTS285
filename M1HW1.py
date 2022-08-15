# CTS 285
# M1HW
# Mary Beth Maraldi
# 8/15/2022


# a for action?
# r for repeat?

a=0
r=1
while a != 5: # allows program to continue until it is exited.
    # choose action to perform
    a = int(input('Main Menu \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exit \nPlease choose a function to perform.'))
    if a == 5: # exits program when required
        print('Goodbye')
        r=5
    else:
        r=1
    
    
    
    while r == 1:
        num1 = int(input('Enter first number'))
        num2 = int(input('Enter second number'))
        print('')
    
        # if addition is requested
        if a == 1: 
        
            print(num1, '+', num2, '=', num1+num2)
            r = int(input('1. Repeat \n2. Main Menu'))
                
        # if subtraction is requested        
        elif a == 2:
           
            print(num1, '-', num2, '=', num1-num2)
            r = int(input('1. Repeat \n2. Main'))
    
                    
        # if multiplication is requested        
        elif a == 3:
         
            print(num1, '*', num2, '=', num1*num2)
            r = int(input('1. Repeat \n2. Main'))
            
        # if divison is requested        
        elif a == 4:
           
            if num2 != 0: # eliminates error
                print(num1, '/', num2, '=', num1/num2)
                
            else:
                print('You can not divide by zero.')
            r = int(input('1. Repeat \n2. Main'))       

