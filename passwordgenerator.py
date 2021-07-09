#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import random
import argparse

def parse_args() -> int:
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-l', '--length',
		help='The length of the password to generate'
	)

	args = parser.parse_args()

	if args.length is not None:
		try:
			return int(args.length)
		except Exception as e:
			print(e.message if hasattr(e, 'message') else e)
			sys.exit(1)
	else:
		print('Error: something went wrong during the parsing of the arguments, aborting')
		sys.exit(1)

def generate_password(characters_sequence: str, password_length: int) -> str:
	return str().join(random.sample(characters_sequence, password_length))

def main():
	length = parse_args()

	if length < 1:
		print('Error: password\'s length can not be less than 1')
		sys.exit(1)

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	symbols = "!?#@{}[]();./_-*&%$"

	password = generate_password(
		lower + upper + numbers + symbols,
		length
	)

	print(password)

if __name__ == "__main__":
	main()
