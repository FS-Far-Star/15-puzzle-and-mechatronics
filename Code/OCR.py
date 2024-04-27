import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr

def perform_ocr():
    print('Performing OCR')
    image = cv2.imread('processed.jpg')
    spacing = 250

    result = np.zeros((4,4))

    reader = easyocr.Reader(['en'])
    num_list = '0123456789'

    # Iterate over the sub-images and perform OCR
    for i in range(4):
        for j in range(4):
            # Extract sub-image
            ocr_input = image[i * spacing: (i + 1) * spacing, j * spacing: (j + 1) * spacing]
            ocr_input = ocr_input[25:225,25:225]
            # plt.imshow(ocr_input,cmap = 'gray')
            # plt.show()

            # Perform OCR
            result_text = reader.readtext(ocr_input, allowlist=num_list,text_threshold=0.3,low_text=0.4)
            
            # Check if any text is detected
            if result_text:
                print(result_text)
                # Print the detected text and probability
                for (bbox, text, prob) in result_text:
                    print(f'Text: {text}, Probability: {prob}')
                    result[i, j] = text
    
    # Verify that 0-15 each appear once
    expected = list(np.arange(0,16))
    print(expected)
    for i in range(4):
        for j in range(4):
            expected.remove(result[i,j])
    if not expected:
        # print(expected)
        flag = True
        
    if flag == True:
        # Save the final result array
        np.savetxt('A_star_solver/initial_state.txt', result, fmt='%d', delimiter=' ')
        print('Initial state obtained and verified')
        # print(result)
    else: 
        print('OCR result invalid, please try again')
    return None
if __name__ == '__main__':
    perform_ocr()

# Note, when I was writing this, easyocr had a lot of problems recognizing 3 and 8. 
# Very frustrating. I tried to modify the preprocessing and eventually got it working. 
# If you are using this, it probably will need fine-tuning. 