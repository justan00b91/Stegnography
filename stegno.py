import os
import sys
from stegano import lsb
from stegano import exifHeader as parser

os.system('clear')

print (' ______________')
print ('< STEGNOGRAPHY >')
print (' --------------')
print ('       \  ^__^')
print ('        \ (oo)\_______')
print ('          (__)\       )\/'+"\\")
print ('               ||----w |')
print ('               ||     ||')
print (' ')
print (' ')

func = (sys.argv[1])
file = (sys.argv[2])+''

if file.endswith('.png'):
	file2 = 'img1.png'
	if func == "-e":
		msg = input('Enter secret message:')
		trans = lsb.hide(file,message=msg)
		trans.save(file2)
		os.remove(file)
		os.rename(file2,file)
		print (' ')
		print ('Message Successfully Hidden!!!')
	if func == "-d":
		message=lsb.reveal(file)
		print (' ')
		print ('The Message Was:')
		print (message)

elif file.endswith('.jpg'):
	file2 = 'photo2.jpg'
	if func == "-e":
		msg = input('Enter secret message:')
		parser.hide(file,file2,msg)
		os.remove(file)
		os.rename(file2,file)
		print (' ')
		print ('Message Successfully Hidden!!!')
	if func == "-d":
		message=parser.reveal(file)
		print ('The Message Was:')
		print (message.decode('utf-8'))

else:
	print('FILE FORMAT NOT SUPPORTED.')
