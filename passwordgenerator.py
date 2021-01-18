#! /usr/bin/env python3

from random import sample
import sys

def generate_password(characters_sequence, password_length) -> str:
	return str().join(sample(characters_sequence, password_length))

def handle_exception():
	sys.exit("[!] Error: Invalid input")

def get_valid_length() -> int:
	while True:
		length = int(input("Enter the length of the password: "))
		if length < 0:
			print("[!] Error: password's length can not be less than 0")
		else:
			break
	return length

def get_password_length() -> int:
	try:
		length = get_valid_length()
	except ValueError:
		handle_exception()
	return length

def main():
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	symbols = "!?#@{}[]();./_-*&%$"

	password = generate_password(
		lower + upper + numbers + symbols,
		get_password_length()
	)

	print("password generated:", password)

if __name__ == "__main__":
	main()
