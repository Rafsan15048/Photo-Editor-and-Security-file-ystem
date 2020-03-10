from tkinter import *
import Functions


############ ..... Main Function ..........
root = Tk()
root.title("Image Editing & File Manager")
#root.configure(background='#597a9b')



### ... Adding a Text for Image editing .....
select_img_btn = Button(root,text = 'Select an Image',command = Functions.Browse_Fun)
select_img_btn.grid(row = 26,column = 7)


edit_image_text = Label(root ,text =' Image Editor')
edit_image_text.grid(row = 0,column = 0)
dummy_textp = Label(root,text = '')



dummy_textp.grid(row = 2,column = 1)


### ... Adding a Text for Image enc & dec .....

encdec_image_text = Label(root ,text  = '     Encryption & Deecryption          ')
encdec_image_text.grid(row = 0,column = 2)


dummy_text1 = Label(root,text = '')
dummy_text2 = Label(root,text = '')
dummy_text3 = Label(root,text = '')
dummy_text4 = Label(root,text = '')
dummy_text5 = Label(root,text = '')
dummy_text6 = Label(root,text = '')
dummy_text7 = Label(root,text = '')
dummy_text8 = Label(root,text = '')
dummy_text9 = Label(root,text = '')
dummy_text9a = Label(root,text = '')
dummy_text10 = Label(root,text = '')
dummy_text11 = Label(root,text = '')
dummy_text12 = Label(root,text = '')
dummy_text13 = Label(root,text = '')
dummy_text14 = Label(root,text = '')
dummy_text15 = Label(root,text = '')
dummy_text16 = Label(root,text = '')
dummy_text17 = Label(root,text = '')
dummy_text18 = Label(root,text = '')
dummy_text19 = Label(root,text = '')


#### ... Adding Button for the Functionality of the Image Editor ...

black_white_btn = Button(root , text  = 'Black and White' , command = Functions.BlackWhite)
black_white_btn.grid(row = 3,column = 0)
dummy_text1.grid(row = 4 ,column = 0 )


auto_contrast_btn = Button(root , text  = 'Auto Contrast' , command = Functions.AutoContrast)
auto_contrast_btn.grid(row = 5,column = 0)
dummy_text2.grid(row = 6 ,column = 0)


blur_btn = Button(root , text  = 'Blur Image' , command = Functions.Blur)
blur_btn.grid(row = 7,column = 0)
dummy_text3.grid(row = 8 ,column = 0)




brightness_btn = Button(root , text  = 'Brightness' , command = Functions.Brightness)
brightness_btn.grid(row = 9,column = 0)
dummy_text4.grid(row = 10 ,column = 0)




contrast_btn = Button(root , text  = 'Contrast Image' , command = Functions.Contrast)
contrast_btn.grid(row = 11 , column = 0)
dummy_text5.grid(row = 12,column = 0)




crop_btn = Button(root , text  = 'Crop Image' , command = lambda : Functions.Crop(crop))
crop_btn.grid(row = 13,column = 0)
dummy_text6.grid(row = 14,column = 0)

crop = StringVar()
crop_entry = Entry(root,textvariable = crop)
crop_entry.grid(row = 13 , column = 1)




edge_detect_btn = Button(root , text  = 'Edge Detection' , command = Functions.EdgeDetection)
edge_detect_btn.grid(row = 15,column = 0)
dummy_text7.grid(row = 16,column = 0)




invert_brn = Button(root , text  = 'Invert Image' , command = Functions.Invert)
invert_brn.grid(row = 17 , column = 0)
dummy_text8.grid(row = 18 , column = 0)




rotate_btn = Button(root , text  = 'Rotate Image' , command = lambda : Functions.Rotate(rotate1))
rotate_btn.grid(row = 19,column = 0)
dummy_text9.grid(row = 20,column = 0)


rotate1 = StringVar()
rotate1_entry = Entry(root,textvariable = rotate1)
rotate1_entry.grid(row = 19 , column = 1)




rotate_btnp = Button(root , text  = 'Rotate Previous Image' , command = Functions.RotatePrevious)
rotate_btnp.grid(row = 21,column = 0)
dummy_text9a.grid(row = 22,column = 0)



threshold_btn = Button(root , text = 'Threshold Image' , command = Functions.Threshold)
threshold_btn.grid(row = 23,column=0)
dummy_text10.grid(row = 24,column = 0)




color_btn = Button(root,text = 'Image Color',command = lambda : Functions.Color(effectImage))
color_btn.grid(row = 25, column = 0)
dummy_text18.grid(row = 26,column = 0)


effectImage = StringVar()
effectImage_entry = Entry(root,textvariable = effectImage)
effectImage_entry.grid(row = 25 , column = 1)





watermark_btn= Button(root , text = 'Watermark & Text' , command = lambda : Functions.Watermark(waterText))
watermark_btn.grid(row = 27,column=0)
dummy_text11.grid(row = 28,column = 0)

waterText = StringVar()
watermark_entry = Entry(root,textvariable = waterText)
watermark_entry.grid(row = 27 , column = 1)





photo_enc_btn = Button(root,text = 'Encrypt Photo',command = Functions.EncryptPhoto)
photo_enc_btn.grid(row = 3, column = 2)
dummy_text12.grid(row = 4,column = 2)

photo_dec_btn = Button(root,text = 'Decrypt Photo',command = Functions.DecryptPhoto)
photo_dec_btn.grid(row = 5, column = 2)
dummy_text13.grid(row = 6,column = 2)



pdf_enc_btn = Button(root,text = 'Encrypt Pdf',command = Functions.EncryptPdf)
pdf_enc_btn.grid(row = 7, column = 2)
dummy_text14.grid(row = 8,column = 2)

pdf_dec_btn = Button(root,text = 'Decrypt Pdf',command = Functions.DecryptPdf)
pdf_dec_btn.grid(row = 9, column = 2)
dummy_text15.grid(row = 10,column = 2)




text_enc_btn = Button(root,text = 'Encrypt text',command = Functions.EncryptText)
text_enc_btn.grid(row = 11, column = 2)
dummy_text16.grid(row = 12,column = 2)

text_dec_btn = Button(root,text = 'Decrypt Text',command = Functions.DecryptText)
text_dec_btn.grid(row = 13, column = 2)
dummy_text17.grid(row = 14,column = 2)




mp3_enc_btn = Button(root,text = 'Encrypt mp3',command = Functions.EncryptMp3)
mp3_enc_btn.grid(row = 15, column = 2)
dummy_text16.grid(row = 16,column = 2)

mp3_dec_btn = Button(root,text = 'Decrypt mp3',command = Functions.DecryptMp3)
mp3_dec_btn.grid(row = 17, column = 2)
dummy_text17.grid(row = 18,column = 2)





root.mainloop()
