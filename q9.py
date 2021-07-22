# Q9 Implement a program dir_tree.py that takes a directory as argument and prints all the files
#    n that directory recursively as a tree. 
#    Hint: Use os.listdir and os.path.isdir functions.

# run in cli by type ->  python q9.py -d env

import argparse
from pathlib import Path
import os

space =  '    '
branch = '│   '
# pointers:
tee =    '├── '

last =   '└── '


def list_all(path):
	files = os.listdir(path)
	subdir_list = str(path).split('/')
	last_space_count = 0
	for i in range(len(subdir_list)):
		if subdir_list[i] != '':
			last_space_count=i
			print(i*space,subdir_list[i],"\n",i*space,last)
	
	for i,file in  enumerate(files):
		print(branch)
		file_path = os.path.join(path,file)
		if os.path.isdir(file_path):
			list_all(file_path)
		else:
			print((last_space_count+1)*space,tee,file)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='That takes a directory as argument and prints all the files n that directory recursively as a tree')
	parser.add_argument('-d', '--dir_info',  
							required = True,
							action ='store', 
							help ='Provide directory name for tree view')

	args     = parser.parse_args()
	dir_name = args.dir_info

	if os.path.isdir(dir_name):
		dir_path 		= Path(dir_name).absolute()
		list_all(dir_path)
			
				
	else:
		print('directory not found!')
	
	
