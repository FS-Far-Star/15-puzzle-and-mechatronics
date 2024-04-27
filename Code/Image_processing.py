import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_preprocess():
    # Read the image
    image = cv2.imread('current_state.jpg')

    # Define the rotation angle (in degrees)
    error = 8 # Camera installation error
    angle = 180 + error # Example rotation angle, adjust as needed
    
    # Define the center of rotation (in this case, the center of the image)
    center = (image.shape[1] // 2, image.shape[0] // 2)

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Perform the rotation
    image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    image = image[850:1850,890:1890] 

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21) 
    
    # # Set average brightness
    # image = image/(np.sum(image)/image.size)*128

    ret3,image = cv2.threshold(image,0,255,cv2.THRESH_OTSU) 

    # Erode + Dilate
    kernel = np.ones((5,5),np.uint8)
    image = cv2.erode(image,kernel,iterations = 1)
    image = cv2.dilate(image,kernel,iterations = 3)
    image = cv2.erode(image,kernel,iterations = 1)
    image = cv2.dilate(image,kernel,iterations = 2)
    image = cv2.erode(image,kernel,iterations = 3)
    image = cv2.dilate(image,kernel,iterations = 2)
    image = cv2.erode(image,kernel,iterations = 2)


    cv2.imwrite('processed.jpg',image)
    print('Processed image saved')
    return None

if __name__ == '__main__':
    image_preprocess()

# image = cv2.imread('processed.jpg')
# # check you are happy with cropping locations
# plt.imshow(image,cmap = 'gray')
# plt.vlines([250,500,750],0,1000)
# plt.hlines([250,500,750],0,1000)
# plt.show()
