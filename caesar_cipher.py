alphabets = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(input_string, shift):
	data = []
	for i in input_string:
		if input_string.strip() and i in alphabets:
			data.append(alphabets[(alphabets.index(i) + shift) % 26])
		else:
			data.append(i)

	output = ''.join(data)
	return output

def main():
	input_string = input('Enter the message: ')
	shift = int(input('Enter the shift: '))
	print(caesar_cipher(input_string, shift))


if __name__ == '__main__':
	main()