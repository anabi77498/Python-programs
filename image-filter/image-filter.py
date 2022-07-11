import sys
from PIL import Image, ImageFilter, ImageOps

'''

input:(format in command line argument) image-filter.py imgfile-name filter-name

output: transformed images based on selected filter

'''

# Transforms image to grayscale rgb values (50,50,50)
def grayscale(img):
    new_img = ImageOps.grayscale(img)
    return new_img

# Flips pixel orientation in image
def flip(img):
    new_img = ImageOps.flip(img)
    return new_img

# Inverts pixel orientation in image
def invert(img):
    new_img = ImageOps.invert(img)
    return new_img

# Mirrors pixel orientation in image
def mirror(img):
    new_img = ImageOps.mirror(img)
    return new_img

# Reduces pixels via BoxBlur -  works by taking each pixel and, giving it a color value that is the average of it's neighbors
def blur(img):
    blurlevel = int(input("Blur level: "))
    new_img = img.filter(ImageFilter.BoxBlur(blurlevel))
    return new_img

# smoothens image thereby reducing sharpness
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

# Options for filter: greyscale, flip, invert, mirror, blur, smooth
op_list = {"grayscale":grayscale, "flip":flip, "invert":invert, 
                "mirror":mirror, "blur":blur, "smooth":smooth}

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