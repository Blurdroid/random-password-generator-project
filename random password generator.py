#import string, random module
import string 
import random

#store all character in list 
s1 = list(string.ascii_lowercase) #abc
s2 = list(string.ascii_uppercase) #ABC
s3 = list(string.digits) #123
s4 = list(string.punctuation) #;'.

#take nuumber from user
character_number = int(input("please enter the number: "))

#make sure that the number is 6 or more using try and except 
while True:
    try: 
        character_number = int(character_number)
        if character_number < 6:
            print("you need at least 6 characters")
            character_number = input("how many character for the password: ")
        else:
            break    
    except:
          print("only numbers please")
          character_number = input("please enter the number: ")
   

#shuffling all lowercase and upper case      
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)     
        
#split 30% and 20% from the user's input
part_1 = round(character_number *(30/100))  #5.4 --> 5  5.6 --> 6
part_2 = round(character_number *(20/100))

password = []

#make a 60% letter and the rest is digits 
for i in range(part_1):
    password.append(s1[i]) 
    password.append(s2[i]) 
       
for i in range(part_2):
    password.append(s3[i]) 
    password.append(s4[i])    

password = "".join(password[0:])

print(password)
