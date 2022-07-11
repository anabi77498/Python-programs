import sys
from PIL import Image, ImageEnhance


'''

input:(format in command line argument) image-filter.py imgfile-name enhance-feature

output: transformed images based on selected enhancement

'''

def brightness(img):
    en_img = ImageEnhance.Brightness(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

def color(img):
    en_img = ImageEnhance.Color(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

def contrast(img):
    en_img = ImageEnhance.Contrast(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

def sharpness(img):
    en_img = ImageEnhance.Sharpness(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img


op_list = {"brightness":brightness, "color":color,
    "contrast":contrast, "sharpness":sharpness}

# ensures that user is adhering to arguments
def argv_check(argv):
    if len(argv) != 3:
        print("\nerror - input command-line argument vector length must be three \n\nformat: \n\"image-filter.py imgfile-name filter-name\"\n")
        sys.exit(1)

    if argv[2].lower() not in op_list:
        print("\nerror - input command must be a filter \n\nformat: \n\"image-filter.py imgfile-name filter-name\"\n")
        print("filters: \n~greyscale \n~flip \n~invert \n~mirror \n~blur \n~smooth\n")
        sys.exit(1)


# main function below

# checks if command argument is valid
argv_check(sys.argv)
try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)

# selects the filter chosen by the user
new_img = op_list[sys.argv[2].lower()](img)

# saves image and gives image name as user input
print("Saving Image as bmp ...")
imagename = input("Image Name: ")
new_img.save(imagename + ".bmp")