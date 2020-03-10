from PIL import  Image , ImageFilter , ImageDraw, ImageFont
import numpy as np
import cv2
import math

from tkinter import filedialog

def Browse_Fun():
    #### ... Opening The file dialog directory to choose a file ...

        file_loc = filedialog.askopenfilename(filetypes = ( ('jpeg file','*.jpg'), ('png file','*.png') ))
        img = Image.open(file_loc)

        #### .. Resizing The Image ..

        if img.size[0] > 1000 :
            img.thumbnail((1000,img.size[1]))
        if img.size[1] > 1000 :
            img.thumbnail((img.size[0],1000))

        img.show()
        img.save(image_name)



def BlackWhite():
    image1 = Image.open(image_name)
    image2 = image1.convert(mode='L')
    image2.save('images/blackwhite.jpg')
    #image2.show()
    img = np.array(image2)
    cv2.imshow('Black&White',img)


def AutoContrast():
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    height = img.shape[0]
    width = img.shape[1]

    min = 255
    max = 0
    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            if a > max:
                max = a
            if a < min:
                min = a

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            b = float(a - min) / (max - min) * 255
            img.itemset((i,j), b)

    cv2.imwrite('images/auto_contrast.jpg', img)

    cv2.imshow('AutoContrast',img)





def Blur():


    image1 = Image.open(image_name)
    image2 = image1.filter(ImageFilter.GaussianBlur(2))
    image2.save('images/blur.jpg')
    image2.show()
    img = np.array(image2)
    cv2.imshow('Blur',img)


def Brightness():
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]

    brightness = 50

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            b = a + brightness
            if b > 255:
                b = 255
            img.itemset((i,j), b)

    cv2.imwrite('images/brightness.jpg', img)

    cv2.imshow('Brightness',img)




def Contrast():
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


def Crop(crop):
    img = Image.open(image_name)
    area = (100,250,1000,700)
    cropped_img = img.crop(area)
    cropped_img.save('images/crop.jpg')
    #img.show()
    cropped_img.show()
    #img = np.array(cropped_img)
    #cv2.imshow('Crop Image',img)



def Invert():
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]

    max_intensity = 255

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            b = max_intensity - a
            img.itemset((i,j), b)

    cv2.imwrite('images/invert.jpg', img)

    cv2.imshow('Invert image',img)


def Rotate(rotate1):
    image1 = Image.open(image_name)
    degree = int (rotate1.get())
    image2=image1.rotate(degree)
    image2.save('images/rotate.jpg')
    image2.show()


def RotatePrevious():
    image1 = Image.open('images/rotate.jpg')
    image2=image1.rotate(90)
    image2.save('images/rotate.jpg')
    image2.show()


def Threshold():
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]

    threshold = 150

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            if a > threshold:
                b = 255
            else:
                b = 0
            img.itemset((i,j), b)

    cv2.imwrite('images/threshold.jpg', img)
    cv2.imshow('image',img)



def EdgeDetection():


    image = Image.open(image_name);
    image2 = image.filter( ImageFilter.FIND_EDGES )
    image2.save('images/edge.jpg')
    image2.show()
    img = np.array(image2)
    cv2.imwrite('images/threshold.jpg', img)
    cv2.imshow('image',img)


def Watermark(waterText):
    image = Image.open(image_name)
    font_type = ImageFont.truetype('C:\Windows\Fonts\CURLZ___.TTF',70)
    draw = ImageDraw.Draw(image)
    draw.text(xy = (620,50),text = waterText.get(),fill = (203,223,241),font = font_type)
    image.show()



def Color(effectimage):

    image = Image.open(image_name)
    overlay = Image.new(image.mode, image.size, color=effectimage.get())
    image2=Image.blend(image, overlay , alpha=0.3)
    image2.save('images/color.jpg')
    image2.show()


def EncryptPhoto():
    fo = open(image_name,"rb")
    image = fo.read()
    fo.close()
    image = bytearray(image)
    key = 48

    for index , value in enumerate(image):
        image[index] = value^key

    fo = open("enc.jpg" , "wb")

    fo.write(image)

    fo.close()




def DecryptPhoto():

    fo = open("enc.jpg","rb")
    image = fo.read()
    fo.close()
    image = bytearray(image)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(image):
        image[index] = value^key

    fo = open("dec.jpg" , "wb")

    fo.write(image)

    fo.close()



def EncryptPdf():
    fo = open("simple.pdf","rb")
    pdf = fo.read()
    fo.close()
    pdf = bytearray(pdf)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(pdf):
        pdf[index] = value^key

    fo = open("enc.pdf" , "wb")

    fo.write(pdf)

    fo.close()



def DecryptPdf():

    fo = open("enc.pdf","rb")
    pdf = fo.read()
    fo.close()
    pdf = bytearray(pdf)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(pdf):
        pdf[index] = value^key

    fo = open("dec.pdf" , "wb")

    fo.write(pdf)

    fo.close()



def EncryptText():

    fo = open("simple.txt","rb")
    text = fo.read()
    fo.close()
    text = bytearray(text)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(text):
        text[index] = value^key

    fo = open("enc.txt" , "wb")

    fo.write(text)

    fo.close()



def DecryptText():

    fo = open("enc.txt","rb")
    text = fo.read()
    fo.close()
    text = bytearray(text)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(text):
        text[index] = value^key

    fo = open("dec.txt" , "wb")

    fo.write(text)

    fo.close()


def EncryptMp3():

    fo = open("simple.mp3","rb")
    mp3 = fo.read()
    fo.close()
    mp3 = bytearray(mp3)
    key = 48 #Provide the user to decrypt the mp3

    for index , value in enumerate(mp3):
        mp3[index] = value^key

    fo = open("encrypt.mp3" , "wb")

    fo.write(mp3)

    fo.close()



def DecryptMp3():

    fo = open("encrypt.mp3","rb")
    mp3 = fo.read()
    fo.close()
    mp3 = bytearray(mp3)
    key = 48 #Provide the user to decrypt the Image

    for index , value in enumerate(mp3):
        mp3[index] = value^key

    fo = open("decrypt.mp3" , "wb")

    fo.write(mp3)

    fo.close()



image_name = 'Selected_Image.jpg'


