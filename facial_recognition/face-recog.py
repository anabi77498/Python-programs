import sys
import numpy as np
from PIL import Image, ImageDraw
import face_recognition as frecog 
import time


def argv_check(argv):

    if len(argv) != 3:
        print("\nERROR - input command argument vector must be of length 3")
        print("Format: face-recog.py known-face-image unknown-face-image\n")
        sys.exit(1)

def selections(question):
    choice = input(question)
    while choice.lower() not in ['yes', 'no']:
        print("\ntype 'yes' or 'no'\n")
        choice = input("Save recognized faces as new image? ")
    return choice.lower()

argv_check(sys.argv)

try:
    train_img = frecog.load_image_file(sys.argv[1])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)

try:
    test_img = frecog.load_image_file(sys.argv[2])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)


print('\nprocessing ...\n')

train_encoding = frecog.face_encodings(train_img)[0]

test_face_locations = frecog.face_locations(test_img)
test_encodings = frecog.face_encodings(test_img, test_face_locations)

new_test_img = Image.fromarray(test_img)

# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(new_test_img)



# Loop through each face found in the unknown image
for (top, right, bottom, left), faces in zip(test_face_locations, test_encodings):

    # See if the face is a match for the known face(s)
    matched_imgs = frecog.compare_faces([train_encoding], faces)

    # Use the known face with the smallest distance to the new face
    distances = frecog.face_distance([train_encoding], faces)

    best_match = np.argmin(distances)

    if matched_imgs[best_match]:

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left - 25, top - 25), (right + 25, bottom + 25)), outline=(255, 0, 0), width=20)
    
        #

# Remove the drawing library from memory as per the Pillow docs
del draw


#

print("\nOpening Saved Images ...")
new_test_img.show()










