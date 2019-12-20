# Importing itertools for iterating through strings
from itertools import starmap, cycle

# Code for Vigenere Cipher
def vigenere_cipher(message, key_stream):
    def single_letter_encrypt(c, k):
        return chr(((ord(k) + ord(c) - 2 * ord('a')) % 26) + ord('a'))
    return ''.join(starmap(single_letter_encrypt, zip(message, cycle(key_stream))))

# Generation of key stream
def generate_key_stream(key, msg):
    store_len = len(msg)
    return(key*int(store_len/len(key)+1))[:store_len]

# Main
def main():
    input_message = input('Enter the string that is to be encrypted: ')
    input_key = input('Enter the key: ')

    if input_message.isalpha() and input_key.isalpha():
        input_message = input_message.lower()
        input_key = input_key.lower()
        
        store_gen_key_stream = generate_key_stream(input_key, input_message)
        print('The key stream is: ', store_gen_key_stream)

        store_encypted_text = vigenere_cipher(input_message, input_key)
        print("The encypted text is: ", store_encypted_text)
    else:
        print('The message and key has to be alphabets [a-z or A-Z] only.\nDon\'t include spaces. \nExiting... \n')
        exit(0)

if __name__ == '__main__':
    main()
