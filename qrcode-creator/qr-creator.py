import sys
import os
import qrcode

'''
input:(format in command line argument) qr-creator.py 'url'

output: qr code that links to inputted url
'''

# ensures that user is adhering to arguments
def argv_check(argv):
    if len(argv) != 2:
        print("\nerror - input command-line argument vector length must be two \n\nformat: \n\"qr-creator.py url \"\n")
        sys.exit(1)

# main function below

# checks if command argument is valid
argv_check(sys.argv)

# selects inputted URL and creates a QR code for it
url = sys.argv[1]
qr = qrcode.make(url)

# saves image as user-inputted name in PNG format and opens QR code
print("Saving Image as png ...")
imagename = input("Image Name: ") + ".png"
qr.save(imagename, "PNG")

os.system("open " + imagename)