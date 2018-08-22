import os
import sys
import re

walk_dir = sys.argv[1]

for root, subdirs, files in os.walk(walk_dir):
    list_file_path = os.path.join(root, 'my-directory-list.txt')

    with open(list_file_path, 'wb') as list_file:
        for filename in files:
            file_path = os.path.join(root, filename)
	    file = open(file_path, "r") 
            content = file.readline()
            m = re.findall('name\d+:(.*)12:piece ',content)
            if (len(m)>0):
              print m[0]


           
