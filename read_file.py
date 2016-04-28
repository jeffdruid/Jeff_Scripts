'''
script for opening a file in our script
and then printing them out
'''

from sys import argv

script = argv

print("Type the file name you would like to open next:")
print("The file should be stored in the same directory as the script ")
file_target = input("> ")
txt_target = open(file_target)

print("Opening File %s" %file_target)
print(txt_target.read())

