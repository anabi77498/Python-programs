import sys
from PIL import Image, ImageFilter, ImageOps


# Options for filter: greyscale, flip, invert, mirror, blur, smooth
opt_list = ["greyscale", "flip", "invert", "mirror", "blur", "smooth"]





def blur(img):
    blurlevel = int(input("Blur level: "))
    new_img = img.filter(ImageFilter.BoxBlur(blurlevel))
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

new_img = blur(img)
print("Saving Image ...")
imagename = input("Image Name: ")
new_img.save(imagename)





#apply filters - from PIL import imagefilter, imageops