# caesar (salad) cipher by Mary Karroqe

def init():	
	pick = raw_input("Would you like to encrypt xor decrypt a message? Type 'e' or 'd': ")
	if pick == "e":
		encrypt()
	elif pick == "d":
		decrypt()
	else:
		print("I said xor, not or... rude.")
		quit()

def main():
	choice = raw_input("Would you like to test another key? Enter 'yes' or 'no'.")
	
	if choice == "yes":
		decrypt()
	elif choice == "no":
		print("k.")
		quit()
	else:
		print("Error :/")
		quit()

	init()

def encrypt():
	plaintext = raw_input("Please enter the message you want to encrypt: ")
	key = raw_input("Please enter your key: ")
	ciphertext = ""
	
	for i in range(0,len(plaintext)):
		x = plaintext[i]
		y = ord(str(x))
		y += int(key)
		ciphertext += chr(y)
	
	print(ciphertext)
	main()

def decrypt():
	plaintext = raw_input("Please enter the message you want to decrypt: ")
	key = raw_input("Please enter your key: ")
	ciphertext = ""

	for i in range(0,len(plaintext)):
		x = plaintext[i]
		y = ord(str(x))
		y -= int(key)
		ciphertext += chr(y)
	
	print(ciphertext)
	main()

init()














