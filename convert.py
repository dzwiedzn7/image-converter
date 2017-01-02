import numpy as np
import scipy.misc as misc


def grey_scale(photo):
    return photo[:,:,0] * 0.299 + photo[:,:,1] * 0.587 + photo[:,:,2] * 0.114


def sepia(picture):
    oR = photo[:,:,0]*.393 + photo[:,:,1]*.769 + photo[:,:,2]*.189
    oG = photo[:,:,0]*.349 + photo[:,:,1]*.686 + photo[:,:,2]*.168
    oB = photo[:,:,0]*.272 + photo[:,:,1]*.534 + photo[:,:,2]*.131
    ort,ogt,obt = oR.T,oG.T,oB.T
    return np.array([ort,ogt,obt]).T


def invert(picture):
    return 255 - picture


def gamma_correction(picture,gamma):
    return picture ** (1./gamma)


def prompt_save_image(picture):
    output_name = raw_input('Enter a name for a new picture: ')
    misc.imsave(output_name, picture)


input_name = raw_input("Enter a name for picture: ")
try:
    picture  = misc.imread(input_name)
    prompt_save_image(grey_scale(picture)) #this part is just for manual test
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
