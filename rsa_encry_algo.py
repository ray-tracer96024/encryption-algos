# This code only contains encryption part and not the decryption part

from Crypto.PublicKey import RSA
import binascii

def main():
    input_message = input('Enter the message to be encrypted [Don\'t include spaces]: ')
    input_bit_length = int(input('Enter the size of the bits [1024, 2048 or 3072]: '))
    generate_key_pair = RSA.generate(input_bit_length)
    public_key = getattr(generate_key_pair.key, 'e')
    private_key = getattr(generate_key_pair.key, 'd')
    extract_mod = getattr(generate_key_pair.key, 'n')

    print('The message is: ', input_message)
    print()
    print('Public Key is: ', public_key)
    print()
    print('[Don\'t share this on the internet] Private Key is: ', private_key)
    print()

    hex_message = binascii.hexlify(input_message.encode())
    print('Hex of ', input_message, ' is: ', hex_message)
    
    print()

    plain_text = int(hex_message, 16)
    print('Plain text: ', plain_text)
    
    print()

    encrypted_text = pow(plain_text, private_key, extract_mod)
    print('Encrypted text: ', encrypted_text)
    
if __name__ == '__main__':
    main()

