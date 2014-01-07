import argparse
import sys
import re
import functions
import urllib2

#
#
#Author: Brendon Ghaderi
#
#

#Parse the arguments from the command line
parser = argparse.ArgumentParser(description='Create an amazing voicemail')
parser.add_argument('-g', help="Gender. It can be either 'male' or 'female'.")
parser.add_argument('-n', help="Phone Number. Any format works.")
parser.add_argument('-r', help="Reasons. Give me a REASON!", type=int)
parser.add_argument('-e', help="Endings. You choose your destiny.", type=int)
parser.add_argument('-o', help="Output file. Just an output file.")
args = parser.parse_args()#get all of the user generated arguments

var = 1
while var == 1:
	outputFile = [];

	#process the Gender
	gender = args.g
	if gender is not None: #Check if null
		gender = gender.lower()
	else :
		print("User forgot to add gender!")
		gender = raw_input("Choose a gender (male/female):")
		if gender is None:
			print("No gender chosen. Terminating the program.")
			sys.exit()

	if gender == "male":
		outputFile.append('f-b1-hello_caller.mp3')
	else:
		outputFile.append('f-b2-lady_at.mp3')

	#process the Phone Number
	phoneNumber = args.n
	if phoneNumber is None: #No number was entered in the command line
		print("No phone number given.")
		phoneNumber = raw_input("Enter a phone number:")
		if phoneNumber is None: #Input for the number was null, terminate the program after giving second chance
			print("No phone number detected. Terminating the program")
			sys.exit() #Exit the program
		else : #Add the number files to the voicemail.mp3 file
			phoneNumber = functions.getPhoneNumber(phoneNumber)
			for num in phoneNumber:
				outputFile.append(str(num)+".mp3")

	else :#Phone number given in the command line. Add the number files to the voicemail.mp3 file
		phoneNumber = functions.getPhoneNumber(phoneNumber)
		for num in phoneNumber:
			outputFile.append(num+".mp3")



	#process the Reasons and add them to the list of files
	#needed to be aggregated to the voicemail.mp3
	reason = args.r
	reasonChoices = []
	if reason is not None: #Reason already given in the command line
		print("Reason given already. No need to display all of the reasons")
		reasonNumbers = str(reason)
		files = functions.getReasonFiles(gender)
		for num in reasonNumbers:
			outputFile.append(files[int(num)])
			reasonChoices.append(files[int(num)])

	else : #No reason in the command line, choose new ones
		functions.displayReasons(gender)
		userInput = raw_input("Please choose your reasons:")
		userInput = re.findall('\d', userInput)
		reasonNumbers = str("".join(userInput))
		files = functions.getReasonFiles(gender)
		for num in reasonNumbers:
			outputFile.append(files[int(num)])
			reasonChoices.append(files[int(num)])

	#process the endings and add them to the list of files
	#needed to be aggregated to the voicemail.mp3
	ending = args.e
	endingChoices = []
	if ending is None: #No ending given in the command line, choose new ones
		functions.displayEndings(gender)
		userInput = raw_input("Please choose your endings:")
		userInput = re.findall('\d', userInput)
		endingNumbers = str("".join(userInput))
		files = functions.getEndingFiles(gender)
		for num in endingNumbers:
			outputFile.append(files[int(num)])
			endingChoices.append(files[int(num)])
	else : #Ending already given in the command line
		userInput = ending
		endingNumbers = str(userInput)
		files = functions.getEndingFiles(gender)
		for num in endingNumbers:
			outputFile.append(files[int(num)])
			endingChoices.append(files[int(num)])

	#Output the results of the person's choice

	print("\nHere is the info you have input")
	print("Gender: "+gender)
	print("Phone : "+"".join(phoneNumber))
	print("\n***************Reason Files Selected***************")
	for reason in reasonChoices :
		print(reason)
	print("*****************************************************")

	print("\n***************Ending Files Selected***************")
	for choice in endingChoices :
		print(choice)
	print("*****************************************************")

	inp = raw_input("\nSatisfied?(y/n): ")
	if inp == "y" :
		break

outputFile.append('m-youre_welcome.mp3')

#process the output file	
outputFileName = args.o
if outputFileName is None:
	print("No output file given, auto writing to the file voicemail.mp3")
	outputFileName = 'voicemail.mp3'

audioFile = open(outputFileName,'w')

#Download the files to create the voicemail file
for item in outputFile :
	print('Attempting to contact: http://www-scf.usc.edu/~chiso/oldspice/'+item)
	response = urllib2.urlopen('http://www-scf.usc.edu/~chiso/oldspice/'+item)
	html = response.read()
	#Write the files to the voicemail.mp3 file
	audioFile.write(html)

audioFile.close()	


#print(args.ops)