#part 1
#nums_int=[1,2,3,4,5]
#for num in nums_int:
# print(nums_int)
 #part 2
#total_height=0
#height_nos=[12,14,16,13,19]
#for height in height_nos:
  #  total_height+=height
#print(total_height)

#total_students=0
#for people in height_nos:
 #  total_students+=1
#print(total_students) 

#avg_height=round(total_height/total_students)
#print(avg_height)

##Part 3
## Finding the Higest no.
#highest_no=0
#nums_int=[1,2,3,4,5]
#for num in nums_int:
 #   if num > highest_no:
  #   highest_no = num
#print(highest_no)    


#Part 4
#printing the even numbers sum using for loop
#sum=0
#for total in range(2,101,2):
 
# sum+=total
 # sum=sum*2
#print(sum)



#import numbers
import random

#import symbol

letters=['A','B','C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X','Y','Z','a', 'b', 'c',' d', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m',' n',' o', 'p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
         


print('Welcome to Password Generator')
no_letters=int(input('How many letters do You want in your Password\n'))
no_symbols=int(input(f"How many symbols do You want in your Password\n"))
no_numbers=int(input(f"How many numbers do You want in your Password\n"))

password=''
for char in range(1,no_letters+1):
 random_char = random.choice(letters)
 password+=random_char

for no in range (1,no_numbers+1):
 password+= random.choice(number)
 
for sym in range (1,no_numbers+1):
 password+=random.choice(symbols) 
 
 
print(password) 
 



















