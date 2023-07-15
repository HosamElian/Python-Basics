from PIL import Image

# open image
myImage = Image.open("test.jpg")

# show
myImage.show()

# My Cropped Image
# left, upper, right, lower
myBox = (0, 0, 20, 20)
myCroppedImage = myImage.crop(myBox)


# show new image
myCroppedImage.show()

# my Converted image 
myConverted = myImage.convert("L")
myConverted.show()