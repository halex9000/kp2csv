###################################################################################################
# Program: kp2csv.py
#  Author: Alessandro Carichini
#    Date: 18-10-18 (1.00)
###################################################################################################
#    Note: Convert kdbx file into csv
#  Modulo: pykeepass
#          https://pypi.python.org/pypi/pykeepass
###################################################################################################
#
from pykeepass import PyKeePass
import sys
import os
import getpass

print("kp2csv:\nConvert kdbx file into csv")

if len(sys.argv) > 1:
	FILE_KDBX = sys.argv[1]
	try:
		PASSW = sys.argv[2]
	except:
		PASSW = getpass.getpass('Insert Password: ')
else:
	print("Usage: kp2csv file.kdbx password")
	sys.exit(1)

entry_count = 0
entry_error = 0

if os.path.isfile(FILE_KDBX):
	FILE_CSV = os.path.splitext(FILE_KDBX)[0]+".csv"
	hfile_CSV = open(FILE_CSV, "w")

	try:
		kp = PyKeePass(FILE_KDBX, password=PASSW)
	except:
		print("FILE ERROR [%s] OR WRONG PASSWORD! " % FILE_KDBX)
		sys.exit(1)

	entries = kp.entries

	hfile_CSV.write("path;title;username;password;url")

	for entry in entries:

		try:
			mypath = entry.path
		except:
			mypath = ""

		try:
			mytitle = entry.title
		except:
			mytitle = ""

		try:
			myusername = entry.username
		except:
			myusername = ""

		try:
			mypass = entry.password
		except:
			mypass = ""

		try:
			myurl = entry.url
		except:
			myurl = ""

		try:
			out_csv = mypath+";"+mytitle+";"+myusername+";"+mypass+";"+myurl+";"
			hfile_CSV.write("\n"+out_csv)
		except:
			print(">>>>>> ERROR UNICODE: %s " % mytitle)
			entry_error = entry_error + 1

		entry_count = entry_count + 1

	print("Entries COUNT %d " % entry_count)
	print("Entries ERROR %d " % entry_error)

	hfile_CSV.close()

else:
	print("NO KEEPASSX FILE [%s]" % FILE_KDBX)

