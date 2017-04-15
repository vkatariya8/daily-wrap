import xml.etree.ElementTree as ET
import os.path
import sys
import shutil
from termcolor import colored
import datetime

def write_date_to_contexts(contexts, paths):
	for c in contexts:
		c_file = open(paths['store_path'] + c + '.txt', 'a')
		c_file.write(datetime.date.today().strftime('%d-%m-%Y') + '\n\n')
		c_file.close()

def read_xml_note(note_file_name, paths):
	tree = ET.parse(paths['adler_notes_path'] + note_file_name)
	root = tree.getroot()
	note_text = root[2].text
	return note_text

def read_txt_note(note_file_name, paths):
	f = open(paths['new_notes_path'] + note_file_name)
	note_text = f.read()
	return note_text

def rename_all_files(paths):
	files = os.listdir(paths['new_notes_path'])
	for file in files:
		if file[-3:] == 'txt':
			#print file
			new_file_name = file.replace(':','-')
			#new_file_name = file.replace('/','-')
			#print new_file_name
			try:
				#shutil.move(file, paths['new_notes_path'] + new_file_name)
				os.rename(paths['new_notes_path'] + file, paths['new_notes_path'] + new_file_name)
			except:
				print new_file_name

def daily_retrieve(contexts, paths):
	files_to_avoid = ['tags.xml']
	files = os.listdir(paths['new_notes_path'])
	i = 0
	for file in files:
		if file not in files_to_avoid:
			if file[-3:] == 'txt':
				if (i%5 == 0):
					print_contexts(contexts)
				try:
					note_text = read_txt_note(file, paths)
					#note_text = read_xml_note(file, paths)
				except:
					note_text = ''
					continue
				print colored(note_text, 'red')
				i+=1
				print_options(["Keep", "Snooze", "Delete", "Rewrite", "Append"])
				keep = raw_input("")
				keep = str.lower(keep[0])
				if keep == 's':
					continue
				src = paths['new_notes_path'] + file
				if keep == 'd':
					del_note(note_text, src, paths)
					continue
				if keep == 'r':
					new_text = raw_input("Write out new text\n")
					note_text = new_text
				if keep == 'a':
					new_text = raw_input("Write out text to be appended\n")
					note_text = note_text + '\n' + new_text
				context = ask_for_context(note_text)
				#print note_text
				contexts = new_context(context, contexts, paths)
				try:
					c_file = open(paths['store_path'] + context + '.txt', 'a')
					c_file.write(note_text + '\n\n')
					c_file.close()
				except:
					print "Error with note "
					print colored(note_text, 'red')
					continue
				shutil.move(src, paths['archive_path'])	
	return contexts

def print_options(options_list):
	for option in options_list:
		print colored(option[0], 'yellow') + option[1:],

def read_contexts():
	context_file = open('contexts.txt', 'r')
	contexts = context_file.read().split('\n')
	contexts = [c for c in contexts if c != '']
	return contexts

def print_contexts(contexts):
	for c in contexts:
		print colored(c, 'green')

def write_contexts(contexts):
	context_file = open('contexts.txt', 'w')
	context_file.truncate()
	for c in contexts:
		context_file.write('\n' + c)

def move_note(note_file_name):
	src = new_notes_path + note_file_name
	dest = archive_path
	shutil.move(src, dest)

def del_note(note_text, src, paths):
	try:
		shutil.move(src, paths['trash_path'])
	except:
		print "Error with note "
		print colored(note_text, 'red')

def ask_for_context(note_text):
	input = raw_input("Add context\n")
	return input

def new_context(context, contexts, paths):
	if str.lower(context) not in contexts:
		contexts.append(str.lower(context))
		c_file = open(paths['store_path'] + context + '.txt', 'w+')
		print "we are here"
		c_file.write(datetime.date.today().strftime('%d-%m-%Y') + '\n')
		c_file.close()
	return contexts

def create_context_aliases(contexts):
	context_dict = {}
	for c in contexts:
		context_dict[c] = str.lower(c[0])
	return contexts, context_dict

'''
def create_context_dict(contexts):
	c_dict = {}
	for c in contexts:
		c_dict[c] = ''
	return c_dict
'''

'''def write_to_context_files(c_dict, paths):
	for c in c_dict:
		c_file = open(paths['store_path'] + c + '.txt', 'w+')
		c_file.write(datetime.date.today().strftime('%d-%m-%Y') + '\n')
		c_file.write(c_dict[c] + '\n')
'''

'''
def move_to_context(note_text, context, c_dict):
	c_dict[context] += (note_text + '\n')
	return c_dict
'''