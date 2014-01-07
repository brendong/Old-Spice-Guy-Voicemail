#functions that are used in the project
import re
import os, os.path

#There are 25 sound files after the 10 digits

def getPhoneNumber(phoneNumber_): #Use the regex module to find all numbers
	search = re.compile('\d') #find only numbers [0-9]
	numbers = search.findall(phoneNumber_)
	return numbers #return an array of the numbers

def getReasons(gender):
	reasons = []
	if gender == "male" :
		reasons = ['Building','Cracking Walnuts','Polishing Monocole','Ripping Weights']
	else :
		reasons = ['Ingesting Old Spice', 'Listening To Reading', 'Lobster Dinner', 'Moon Kiss', 'Riding A Horse']
	return reasons

def getReasonFiles(gender):
	reasonFiles = []
	if gender == "male" :
		reasonFiles = ['m-r1-building.mp3', 'm-r2-cracking_walnuts.mp3', 'm-r3-polishing_monocole.mp3', 'm-r4-ripping_weights.mp3']
	else :
		reasonFiles = ['f-r1-ingesting_old_spice.mp3', 'f-r2-listening_to_reading.mp3', 'f-r3-lobster_dinner.mp3', 'f-r4-moon_kiss.mp3', 'f-r5-riding_a_horse.mp3']

	return reasonFiles


def displayReasons(gender): #Display the menu for choosing the reasons
	print("Reasons Menu")
	reasons = getReasons(gender)
	index = 0
	for reason in reasons :
		print("["+str(index)+"] "+reason)
		index = index + 1

def getAllFiles() : #return an array of all the files
	return [name for name in os.listdir('Sounds') ]


def getEndings(gender) :
	endings = []
	if gender == "male" :
		endings = ['Horse', 'Jingle', 'On Phone', 'Swan Dive', 'Voicemail']
	else :
		endings = ['She will get back to you', 'Thanks For Calling']

	return endings

def getEndingFiles(gender) :
	endings = []
	if gender == "male":
		endings = ['m-e1-horse.mp3', 'm-e2-jingle.mp3', 'm-e3-on_phone.mp3', 'm-e4-swan_dive.mp3', 'm-e5-voicemail.mp3']
	else :
		endings = ['f-e1-she_will_get_back_to_you.mp3', 'f-e2-thanks_for_calling.mp3']

	return endings

def displayEndings(gender): #Display the menu for choosing the endings
	print("Endings Menu")
	reasons = getEndings(gender)
	index = 0
	for reason in reasons :
		print("["+str(index)+"] "+reason)
		index = index + 1


	