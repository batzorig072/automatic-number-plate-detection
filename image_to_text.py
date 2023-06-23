import easyocr
import cv2
from matplotlib import pyplot as plt
import glob

reader = easyocr.Reader(['mn'])




for imagePath in glob.glob('./runs/plates/**/*.jpg'):
  finalResult = ""
  result = reader.readtext(imagePath)
  img = cv2.imread(imagePath)
  spacer = 100

  for detection in result:
    top_left = tuple([int(detection[0][0][0]), int(detection[0][0][1])])
    bottom_right = tuple([int(detection[0][2][0]), int(detection[0][2][1])])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    spacer+=15
    finalResult = finalResult + detection[1]

  cv2.imwrite("./runs/ocr/" + finalResult + ".jpg", img)
