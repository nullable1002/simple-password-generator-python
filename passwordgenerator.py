#! /usr/bin/env python3

from random import sample
import sys

def generate_password(characters_sequence, password_length):
	return "".join(sample(characters_sequence, password_length))
	
def main():
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	symbols = "!?#@{}[]();./_-*&%$"

	characters = lower + upper + numbers + symbols
	try:
		length = int(input("Enter the length of the password: "))
	except:
		sys.exit("Error: Invalid input")
	
	password = generate_password(characters, length)

	print("password generated: ", password)

if __name__ == "__main__":
	main()
