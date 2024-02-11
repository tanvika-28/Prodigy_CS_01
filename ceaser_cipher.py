letters='abcdefghijklmnopqrstuvwxyz'
num_letters =len(letters)

def encrypt(plaintext,key):
    ciphertext =''
    for letter in plaintext:
        letter = letter.lower()
        if not letter =='':
            index =letters.find (letter)
            if index == -1:
                 ciphertext += letter
            else:
                new_index = index + key 
                if new_index>=num_letters:
                    new_index -=num_letters
                ciphertext += letters[new_index]
    return  ciphertext 
def decrypt(ciphertext,key):
    plaintext =''
    for letter in plaintext:
        letter = letter.lower()
        if not letter =='':
            index =letters.find (letter)
            if index == -1:
                 ciphertext += letter
            else:
                new_index = index - key 
                if new_index< 0:
                    new_index -=num_letters
                plaintext += letters[new_index]
    return  plaintext   
def  encrypt_decrypt(text,mode,key):
    result =''
    if mode =='d':
        key =-key            
    for letter in text:
        letter =letter.lower()
        if not letter =='':
            index = letters.find(letter)
            if index == -1:
                result += letter 
            else:
                new_index = index + key 
                if new_index>= num_letters:
                    new_index -= num_letters
                elif new_index < 0 :
                    new_index += num_letters  
                result += letters[new_index]         
    return result    
                
         
    
print('ceaser cipher program')
print('Do you want to encrypt or Decrypt?')
user_input = input('e/d:').lower()

if user_input == 'e':
    print('Encryption mode selected')
    
    key =int(input('Enter the key (1 through 26):'))
    text =input('Enter the text to encrypt:')
    ciphertext =encrypt_decrypt(text,user_input,key)
    print (f'ciphertext:{ciphertext}')

elif user_input   == 'd':
    print('Decryption mode selected')
    
    key =int(input('Enter the key (1 through 26):'))
    text =input('Enter the text to decrypt:')
    plaintext =encrypt_decrypt(text,user_input,key)
    print (f'plaintext:{plaintext}')

  