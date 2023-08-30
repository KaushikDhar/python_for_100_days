# function with 2 inputs(part1)
#def opp_function(name1,location):
 # print(f"hiii,{name1}")
 # print("o hello bro")
 # print("where are u going")
 # print(f"I am going to {location}")
    
    
#opp_function("Kaushik","Agartala")



#for chow in range(0,5+1):
 
 #print("chow")==
 
 #Part2
 
#def cover_paint(height,width,cover):
#    paint=round((height*width)/cover)
 #   print(paint)
    
    
#cover_paint(4,5,3)    

#prime no. checker
#def prime_check(n):
#    is_prime=True
 #   for i in range(2,n):
  #   if n%i==0 :
   #   is_prime=False  
    ##   print("A prime no.")
    ###  
#prime_check(7)   

#project
#from turtle import position

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

    
def encryption(plain_text,shift_ammount):
    cifer_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_ammount
        new_letter=alphabet[new_position]
        cifer_text+=new_letter
    print(f"your encoded message is {cifer_text}")   
    
     
encryption(plain_text=text,shift_ammount=shift)

def decryption(cipher_text,shift_ammount):
    plain_text=''
    for letter in cipher_text:
        position=alphabet.index[letter]
        new_position=position-shift_ammount
        plain_text+=alphabet[new_position]
    print(f"your decoded message is {plain_text}")    
    
    
if direction=="encode":
    encryption(plain_text=text,shift_ammount=shift)
elif direction=="decode":
    decryption(cipher_text=text,shift_ammount=shift)
    
    
    