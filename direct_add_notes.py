from termcolor import colored
import os
import datetime
from variables import paths


def add_note(paths):
	note_text = raw_input(colored("Enter note text.\n", "yellow"))
	file_short = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")
	counter = 0
	while (1):	
		#print os.path.isfile(paths['new_notes_path'] + file_short + '.txt')
		if(os.path.isfile(paths['new_notes_path'] + file_short + '.txt') == False):
			f = open(paths['new_notes_path'] + file_short + '.txt', 'w+')
			#print file_short
			break
		file_short = file_short + '-1'
		#f = open(paths['new_notes_path'] + file_short + '.txt', 'w+')
		counter += 1
	f.write(note_text)
	return 0


while 1:
	add_note(paths)