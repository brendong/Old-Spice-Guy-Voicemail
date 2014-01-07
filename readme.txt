Author: Brendon Ghaderi

The program creates a voicemail recording using mp3 clips of the "old spice guy." 

Example command line call: $python test.py -g male -n 8055555555 -r 12 -e 1 -o voicemail.mp3

To use the program:
	1. Open up terminal and enter "python test.py" with the values that you want
	2. You can either leave the arguments empty or fill them on the call of the file
	3. The parameters are:
		*-h : for help
		*-g : set Gender
		*-n : set the number for the voicemail
		*-r : set the reasons (i.e 12, 123, 23)
		*-e : set the endings (i.e 1, 23, 32)
		*-o : set the name of the voicemail recording file
	4. If you do not wish to do all of that on the command line, you can just press enter and the program will prompt you for each value.

Notes:
	The program has a gender flag. This variable determines which responses and endings you can choose from as there are personalized responses for each gender.

	Sources used: 
	http://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist

	http://stackoverflow.com/questions/4706499/how-do-you-append-to-file-in-python

	http://www-scf.usc.edu/~chiso/oldspice/

	*All code is commented and laid out neatly