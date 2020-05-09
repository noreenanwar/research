import cv2
import glob
import os
inputfolder= 'data'
folderLen= len(inputfolder)
os.mkdir('Resized1')
for img in glob.glob(inputfolder +"/*.jpg"):
    image=cv2.imread(img)
    imgResized =cv2.resize(image,(550,550))
    cv2.imwrite("Resized1"+ img[folderLen:],imgResized)
    cv2.imshow('image', imgResized)
    cv2.waitKey(30)


cv2.destroyAllWindows()