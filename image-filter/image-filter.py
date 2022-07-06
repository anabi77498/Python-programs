import sys
from PIL import Image, ImageFilter, ImageOps


# Options for filter: greyscale, flip, invert, mirror, blur, smooth
opt_list = ["grayscale", "flip", "invert", "mirror", "blur", "smooth"]


def grayscale(img):
    new_img = ImageOps.grayscale(img)
    return new_img

def flip(img):
    new_img = ImageOps.flip(img)
    return new_img

def invert(img):
    new_img = ImageOps.invert(img)
    return new_img

def mirror(img):
    new_img = ImageOps.mirror(img)
    return new_img

def blur(img):
    blurlevel = int(input("Blur level: "))
    new_img = img.filter(ImageFilter.BoxBlur(blurlevel))
    return new_img

def smooth(img):
    choice = 0
    while True:
        choice = int(input("Smooth level (choose 1 or 2): "))
        if choice in [1,2]:
            break
    if choice == 1:
        new_img = img.filter(ImageFilter.SMOOTH)
    elif choice == 2:
        new_img = img.filter(ImageFilter.SMOOTH_MORE)
    return new_img


def argv_check(argv):
    if len(argv) != 3:
        print("\nerror - input command-line argument must be three \n\nformat: \n\"image-filter.py imgfile-name filter-name\"\n")
        sys.exit(1)

    if argv[2] not in opt_list:
        print("\nerror - input command must be a filter \n\nformat: \n\"image-filter.py imgfile-name filter-name\"\n")
        print("filters: \n~greyscale \n~flip \n~invert \n~mirror \n~blur \n~smooth\n")
        sys.exit(1)


argv_check(sys.argv)
try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)

if sys.argv[2] == 'grayscale':
    new_img = grayscale(img)
if sys.argv[2] == 'flip':
    new_img = flip(img)
if sys.argv[2] == 'invert':
    new_img = invert(img)
if sys.argv[2] == 'mirror':
    new_img = mirror(img)
if sys.argv[2] == 'blur':
    new_img = blur(img) 
if sys.argv[2] == 'smooth':
    new_img = smooth(img) 

print("Saving Image ...")
imagename = input("Image Name: ")
new_img.save(imagename)