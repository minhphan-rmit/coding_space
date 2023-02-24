import os

# input from user
mess = input('Your message: ')
file_name = input('Your file name: ')
folder_name = input('Your folder name: ')

# create file path
file_path = folder_name + '\\' + file_name
# create folder
os.makedirs(folder_name, exist_ok=True)
# generate 100 lines of message
mess = (mess + '\n') * 100
# open file to write
f = open(file_name, 'w')
# write messages to the file
f.write(mess)
# close the file
f.close()


