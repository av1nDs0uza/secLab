# Substitution Cipher 
import string

# list containing all strings
all_letters = string.ascii_letters

# create a dictionary to store the substitution for plaintext

dict1 ={} 
key = 4 

for i in range (len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
    
plainText = "I am in Securtiy practical"
cipherText=[]

# loop to generate cipherText

for char in plainText:
    if char in all_letters:
        temp = dict1[char]
        cipherText.append(temp)
    else:
        temp = char
        cipherText.append(temp)
        
cipherText = "".join(cipherText)
print("Cipher text is :",cipherText)

#create a dictionary to store the substitution
#for the given alphabet in the cipher
#text based on the key

dict2 ={}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
    
# loop to recover plaintext
decryptText =[]

for char in cipherText:
    if char in all_letters:
        temp = dict2[char]
        decryptText.append(temp)
    else:
        temp = char
        decryptText.append(temp)

decryptText = "".join(decryptText)
print("Recovered plain text :", decryptText)
     