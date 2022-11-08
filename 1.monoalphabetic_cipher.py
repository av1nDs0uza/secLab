freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 
'x', 'q', 'z']

cipherText = 'slaztllaavupnoahaaolwhyr'

occurance = {}

for symbol in cipherText:
    if symbol in occurance:
        occurance[symbol]  += 1
    else:
        occurance[symbol] = 1

print(occurance)

def decryption(cipherText, k):
    plainText =""
    for symbol in cipherText:
        pt = (ord(symbol) - 97 -k)%26
        pt = chr(pt+97)
        plainText += "".join(pt)
    print(f"{letter}; PlainText: {plainText}")

word = max(occurance, key=occurance.get)
print(word)

for letter in freq:
    k = (ord(word) - ord(letter))%26
    decryption(cipherText, k)