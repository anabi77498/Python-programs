# Accessed Libraries
import sys
import numpy as np
from PIL import Image, ImageDraw
import face_recognition as frecog 
import time

# Function that checks command-line-argument 
def argv_check(argv):
    if len(argv) != 3:
        print("\nERROR - input command argument vector must be of length 3")
        print("Format: face-recog.py known-face-image unknown-face-image\n")
        sys.exit(1)

# Function that prompts user for yes or no answer
def selections(question):
    choice = input(question)
    while choice.lower() not in ['yes', 'no']:
        print("\ntype 'yes' or 'no'\n")
        choice = input(question)
    return choice.lower()

# Function that implements deep-learning program from dlib library
def HOG_model(train_img, test_img):

    '''
    Function that implements deep-learning program from dlib library
    powered by HOG_model with a accuracy of 99.38% on the Labeled Faces in the Wild benchmark
    
    input: image for model to use as basis for recognition (known image) 
           image for model to implement recognition (unknown image)

    output: image of seperate recognized face 
            image of recognized face in unknown image     
    '''

    #encoding known image
    train_encoding = frecog.face_encodings(train_img)[0]

    #storing locations of ALL recognized faces from unknown image
    test_face_locations = frecog.face_locations(test_img)

    #encoding ALL recognized faces in unknown image
    test_encodings = frecog.face_encodings(test_img, test_face_locations)
    new_test_img = Image.fromarray(test_img)

    # Create a Pillow ImageDraw Draw instance to draw on unknown image
    draw = ImageDraw.Draw(new_test_img)

    # Looping through each individual face found in unknown image
    for (top, right, bottom, left), faces in zip(test_face_locations, test_encodings):

        # comparing face in known image to each fdace in unknown image
        matched_imgs = frecog.compare_faces([train_encoding], faces)

        # selecting best match face based
        distances = frecog.face_distance([train_encoding], faces)
        best_match = np.argmin(distances)

        if matched_imgs[best_match]:

            # Draw a box around the face using the Pillow module
            draw.rectangle(((left - 25, top - 25), (right + 25, bottom + 25)), outline=(255, 0, 0), width=20)

            # location of matched face
            facelocation = test_img[top:bottom, left:right]
            found_face = Image.fromarray(facelocation)

            # deleting draw for memory optimization
            del draw

            # returning image of found face and the image drawn on
            return found_face, new_test_img


# MAIN BELOW

#checking command line argument
argv_check(sys.argv)

# checking access to image in argvector[1]
try:
    train_img = frecog.load_image_file(sys.argv[1])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)

# checking access to image in argvector[2]
try:
    test_img = frecog.load_image_file(sys.argv[2])
except FileNotFoundError:
    print("\nError - File not found \n\nMake sure file name is correct and in the script's directory\n")
    sys.exit(2)

# checking if inputted images are correct
print('\nKnown image: ' + sys.argv[1])
print('Unknown image: ' + sys.argv[2] + '\n')
check = selections('Is this correct: ')

# aborting program if inputted images are incorrect
if check == 'no':
    print('\nAborting program ...')
    print("Command Line Format: face-recog.py known-face-image unknown-face-image\n")
    sys.exit(1)

print('\nprocessing images ...\n')

# Implementing model to find faces of uploaded image
found_face, new_test_img = HOG_model(train_img, test_img)

# option to save image of face only
choice_newimg = selections("Save recognized faces as seperate new image? ")
if choice_newimg == 'yes':
    name_n = input("Image name: ")
    print('\nSaving ' + name_n +  ' as PNG ...\n')
    found_face.save(name_n + '.PNG')

# option to save image image drawn on
choice_save = selections("Save modified image as new image? ")
if choice_save == 'yes':
    name_s = input("Image name: ")
    print('\nSaving ' + name_s + ' as PNG ...')
    new_test_img.save(name_s + '.PNG')

# opening found faces
print("\nOpening images ...")
new_test_img.show()
found_face.show()










