#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
