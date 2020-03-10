from PIL import  Image , ImageFilter , ImageDraw, ImageFont
import numpy as np
import cv2
import math

img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]

    contrast = 1.3

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            b = math.ceil(a * contrast)
            if b > 255:
                b = 255
            img.itemset((i,j), b)

    cv2.imwrite('images/contrast.jpg', img)

    cv2.imshow('Contrast Image',img)
