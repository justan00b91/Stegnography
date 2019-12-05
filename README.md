# Stegnography using Python

* ## Requirements:
The code requires python3 installed along with stegano library.
To install stegano library:
 ```bash
 sudo pip install stegano
 ```
 
* ## Usage:
To encode messages:
```bash
python3 stegno.py -e [image name].[file extension]
```
to decode messages:
```bash
python3 stegno.py -d [image name].[file extension]
```

* ## Description:
The following code takes an image as input and an option (e or d) along with it.
Then using stegano library, it hides or reveals the message according to the user choice.
The code runs separately for PNG and JPG files and prints the result accoudingly.
The code for PNG is:

```python
from stegano import lsb

file2 = 'img1.png'
	if func == "-e":
		msg = input('Enter secret message:')
		trans = lsb.hide(file,message=msg)
		trans.save(file2)
		os.remove(file)
		os.rename(file2,file)
	if func == "-d":
		message=lsb.reveal(file)
```
The code for JPG is:

```python
from stegano import exifHeader as parser

file2 = 'photo2.jpg'
	if func == "-e":
		msg = input('Enter secret message:')
		parser.hide(file,file2,msg)
		os.remove(file)
		os.rename(file2,file)
	if func == "-d":
		message=parser.reveal(file)
```
* ## Output:
For encoding messages:
```bash
Enter secret-message:+++++++++++++++
Message Successfully Hidden!!!
```
For decoding messages:
```bash
The Message Was:
+++++++++++++++
```
