#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
import string

def alphabetsRange(c1, c2):
    
    alphabetRange = []
    
    #creating list of alphabets from with ascii
    for c in range(ord(c1), ord(c2) + 1):
        alphabetRange.append(chr(c))
    
    return alphabetRange


def randomPasswordGenerator(minLength, maxLength, passwordLengthOptional=0):
    
    #creates a password that is atleast minLength long and utmost maxLength long 
    #with a password length that is optional 
    
    alphaSmallList = alphabetsRange('a', 'z')
    alphaCapitalList = alphabetsRange('A', 'Z')
    numericsList = list(range(0, 10)) #creates a list from 0 to 9
    specialCharactersList = list(string.punctuation)
    
    password = []
    
    #password should have atleast 1 small character, 1 upper case, 1 special character, and 1 number
    password.append(random.choice(alphaSmallList))
    password.append(random.choice(alphaCapitalList))
    password.append(random.choice(numericsList))
    password.append(random.choice(specialCharactersList))
    
    combinedCharacters = alphaSmallList + alphaCapitalList + numericsList + specialCharactersList
    #random passwordLength if not set by the user
    if passwordLengthOptional == 0:
        passwordLength = random.choice(list(range(minLength, maxLength+1)))
    else:
        passwordLength = passwordLengthOptional
    
    while (len(password) < passwordLength):
        password.append(random.choice(combinedCharacters))
        
    passwordNew = random.sample(password, len(password))
    
    return ''.join(str(e) for e in passwordNew)


def isLengthDigitValidation(input):
    return input.isdigit()


def inputFunction():
    minLength = input('Enter min length for password: ')
    if(isLengthDigitValidation(minLength) and not(int(minLength)==0)):
        maxLength = input('Enter max length for password: ')
        if(isLengthDigitValidation(maxLength) and not(int(minLength)==0)):
            if(int(maxLength) > int(minLength)):
                optionalLength = input('Your preferred password length (Optional- if not required, input 0): ')
                if(isLengthDigitValidation(optionalLength)):
                    if(int(optionalLength) >= int(minLength) and int(optionalLength) <= int(maxLength)):
                        generatedPassword = randomPasswordGenerator(int(minLength), int(maxLength), int(optionalLength))
                        print('Password Length = ', len(generatedPassword))
                        print('Generated Password\n', generatedPassword)
                    else:
                        print('ERROR! Please enter an integer between min length and max length!')
                else:
                    print('ERROR! Please enter an integer!')
            else:
                print('ERROR! Your max length has to be greater than your min length')
        else:
            print('ERROR! Please enter an integer greater than 0!')
    else:
        print('ERROR! Please enter an integer greater than 0!')
        

#start of the main function
inputFunction()


# In[ ]:





# In[ ]:




