import hashlib

def sha256():
	input_string = input('Enter the message: ')
	r1 = hashlib.sha256(input_string.encode())
	print('The hash in hex form is: ', r1.hexdigest())
	exit(0)

def sha3_256():
	input_string = input('Enter the message: ')
	r2 = hashlib.sha3_256(input_string.encode())
	print('The hash in hex form is: ', r2.hexdigest())
	exit(0)

def sha3_384():
	input_string = input('Enter the message: ')
	r3 = hashlib.sha3_384(input_string.encode())
	print('The hash in hex form is: ', r3.hexdigest())
	exit(0)

def sha224():
	input_string = input('Enter the message: ')
	r4 = hashlib.sha224(input_string.encode())
	print('The hash in hex form is: ', r4.hexdigest())
	exit(0)

def blake2b():
	input_string = input('Enter the message: ')
	r5 = hashlib.blake2b(input_string.encode())
	print('The hash in hex form is: ', r5.hexdigest())
	exit(0)

def shake_256():
	input_string = input('Enter the message: ')
	r6 = hashlib.shake_256(input_string.encode())
	print('The hash in hex form is: ', r6.hexdigest())
	exit(0)

def sha384():
	input_string = input('Enter the message: ')
	r7 = hashlib.sha384(input_string.encode())
	print('The hash in hex form is: ', r7.hexdigest())
	exit(0)

def shake_128():
	input_string = input('Enter the message: ')
	r8 = hashlib.shake_128(input_string.encode())
	print('The hash in hex form is: ', r8.hexdigest())
	exit(0)

def sha1():
	input_string = input('Enter the message: ')
	r9 = hashlib.sha1(input_string.encode())
	print('The hash in hex form is: ', r9.hexdigest())
	exit(0)

def sha512():
	input_string = input('Enter the message: ')
	r10 = hashlib.sha512(input_string.encode())
	print('The hash in hex form is: ', r10.hexdigest())
	exit(0)

def md5():
	input_string = input('Enter the message: ')
	r11 = hashlib.md5(input_string.encode())
	print('The hash in hex form is: ', r11.hexdigest())
	exit(0)

def sha3_512():
	input_string = input('Enter the message: ')
	r12 = hashlib.sha3_512(input_string.encode())
	print('The hash in hex form is: ', r12.hexdigest())
	exit(0)

def blake2s():
	input_string = input('Enter the message: ')
	r13 = hashlib.blake2s(input_string.encode())
	print('The hash in hex form is: ', r13.hexdigest())
	exit(0)

def sha3_224():
	input_string = input('Enter the message: ')
	r14 = hashlib.sha3_224(input_string.encode())
	print('The hash in hex form is: ', r14.hexdigest())
	exit(0)

def show_options():
	print('1. sha256 \n2. sha3_256 \
		 	\n3. sha3_384 \n4. sha224 \n5. blake2b \n6. shake_256 \
		 	\n7. sha384 \n8. shake_128 \n9. sha1 \n10. sha512 \n11. md5 \n12. sha3_512 \
		 	\n13. blake2s \n14. sha3_224')


def switch(option):
	switcher = {
		1 : sha256(), 2 : sha3_256(), 3 : sha3_384(), 4 : sha224(), 5 : blake2b(), 6 : shake_256(), 
		7 : sha384(), 8 : shake_128(), 9 : sha1(), 10 : sha512(), 
		11 : md5(), 12 : sha3_512(), 13 : blake2s(), 14 : sha3_224()
	}
	switcher.get(option, 'Invalid option')


def main():
	show_options()
	option = int(input('Enter the encryption standard: '))
	switch(option)


if __name__ == '__main__':
	main()