# caesar (salad) cipher by Mary Karroqe

def init():	
	pick = raw_input("Would you like to encrypt xor decrypt a message? Type 'e' or 'd': ")
	if pick == "e":
		encrypt()
	elif pick == "d":
		decrypt()
	else:
		print("I said xor, not or... rude.")
		exit()

def main():
	choice = raw_input("Would you like to test another key? Enter 'yes' or 'no'. ")
	
	if choice == "yes":
		decrypt()
	elif choice == "no":
		print("k.")
		quit()
	else:
		print("Error :/ ")
		quit()

	init()
'''
def main2():
	choice = raw_input("Would you like to decrypt your message? Enter 'yes' or 'no'. ")
    if choice == "yes":
        print("Aha.. I see you don't trust me.  That's okay, here's the original message: ")
        decrypt()
    elif choice == "no":
        print("k.")
        quit()
    else:
        print("Error. Way to break me :/")
'''
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

def decrypt():
	plaintext = raw_input("Please enter the message you want to decrypt: ")
	ifkey = raw_input("Would you like to enter a key? 'yes' or 'no': ")
	key = ""
	ciphertext = ""

	if ifkey == 'yes':
		key = raw_input("Please enter your key: ")

		for i in range(0,len(plaintext)):
			x = plaintext[i]
			y = ord(str(x))
			y -= int(key)
			ciphertext += chr(y)

		print(ciphertext)

	elif ifkey == 'no':
		print("Testing all possible solutions...")

		for i in range(1, 32):

			key = i

			for j in range(0,len(plaintext)):
				x = plaintext[j]
				y = ord(str(x))
				y -= int(key)
				ciphertext += chr(y)

			print(key)	
			print(ciphertext + "\n")

			ciphertext = ""

init()
