import sys
from PIL import Image, ImageEnhance

'''

input:(format in command line argument) image-filter.py imgfile-name enhancement

output: transformed images based on selected enhancement

'''

# Enhances brightness of image by a designated factor
def brightness(img):
    en_img = ImageEnhance.Brightness(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

# Enhances color (vibrance) of image by a designated factor
def color(img):
    en_img = ImageEnhance.Color(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

# Enhances contrast of image by a designated factor
def contrast(img):
    en_img = ImageEnhance.Contrast(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

# Enhances sharpness of image by a designated factor
def sharpness(img):
    en_img = ImageEnhance.Sharpness(img)
    factor = int(input("Enhance factor: "))
    new_img = en_img.enhance(factor)
    return new_img

# list of possible operations: brightness, color, contrast, sharpness
op_list = {"brightness":brightness, "color":color,
    "contrast":contrast, "sharpness":sharpness}

# ensures that user is adhering to arguments
def argv_check(argv):
    if len(argv) != 3:
        print("\nerror - input command-line argument vector length must be three \n\nformat: \n\"image-filter.py imgfile-name enhancement-name\"\n")
        sys.exit(1)

    if argv[2].lower() not in op_list:
        print("\nerror - input command must be a filter \n\nformat: \n\"image-filter.py imgfile-name enhancement-name\"\n")
        print("enhancements: \n~brightness \n~color \n~contrast \n~sharpness\n")
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