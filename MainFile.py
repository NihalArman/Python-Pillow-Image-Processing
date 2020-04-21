from PIL import Image, ImageEnhance

#READ IMAGE
img = Image.open("input/409.png")
# img.show()

# #PRINT IMAGE SIZE
# print(img.size) #size of the image
#
#
# #PRINT IMAGE FORMAT
# print(img.format) #format of the image


#PRINT IMAGE
#img.show() #show image


# #ROTATE IMAGE--------------------------------------
# angle = 45
# #rotated_img = img.rotate(angle) #only rotate
# rotated_img = img.rotate(angle, expand=True) #rotate and adjust the output size
# rotated_img.show()
# #ROTATE IMAGE--------------------------------------


# #CROPPING IMAGE -------------------------------------
# #area selection
# area = (0, 100, 270, 275)
# cropped_img = img.crop(area) #crop image
# cropped_img.show()
# #cropped_img.save('croppedimage.png') #saves the image
# # Cropping done--------------------------------------



# #RESIZE Image
# size = (200,200)
# box = (100,100,500,400)
# #normal resize
# resized_img = img.resize(size)
# #resize with box
# resized_img_withbox = img.resize(size, box=box)
# #print
# resized_img.show();
# resized_img_withbox.show();



# #ADJUST IMAGE Brightness -----------------------------------
# #image brightness enhancer
# enhancer = ImageEnhance.Brightness(img)
#
# factor = 1 #gives original image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('contrastcheck.png') #saves the image
#
# factor = 0.5 #darkens the image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('contrastcheck.png') #saves the image
#
# factor = 1.5 #brightens the image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('contrastcheck.png') #saves the image
# #ADJUST IMAGE Brightness DONE-----------------------------------



# #ADJUST IMAGE Sharpness -----------------------------------
# #image sharpness enhancer
# enhancer = ImageEnhance.Sharpness(img)
#
# factor = 1 #gives original image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('sharpnesscheck.png') #saves the image
#
# factor = 0.5 #darkens the image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('sharpnesscheck.png') #saves the image
#
# factor = 4.5 #brightens the image
# img_output = enhancer.enhance(factor)
# img_output.show()
# #img_output.save('sharpnesscheck.png') #saves the image
# #ADJUST IMAGE Sharpness DONE-----------------------------------



#ADJUST IMAGE Contrast -----------------------------------
#image sharpness enhancer
enhancer = ImageEnhance.Contrast(img)

factor = 1 #gives original image
img_output = enhancer.enhance(factor)
img_output.show()
#img_output.save('contrastcheck.png') #saves the image

factor = 0.5 #darkens the image
img_output = enhancer.enhance(factor)
img_output.show()
#img_output.save('contrastcheck.png') #saves the image

factor = 4.5 #high contrasted the image
img_output = enhancer.enhance(factor)
img_output.show()
#img_output.save('contrastcheck.png') #saves the image
#ADJUST IMAGE Contrast DONE-----------------------------------
#--------------------------------------------------------------------------------------------------------------------
