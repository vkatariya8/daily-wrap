import datetime
from variables import paths
import os

files = os.listdir(paths['desktop_path'])
files = [f for f in files if f[-3:] == 'txt']
for f in files:
	src = paths['desktop_path'] + f
	print "Current date file is ", f[:-4]
	
	#shutil.move(src, paths['archive_path'])