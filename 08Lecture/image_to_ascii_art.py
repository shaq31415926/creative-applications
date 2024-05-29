import cv2
import pygame as pg
from helpers import get_image, draw_converted_image, save_image, resize_cv2_image

path = "image/marguerite-729510_1280.jpeg"
#image = cv2.imread(path)
image = get_image(path, rgb=False)
# image = resize_cv2_image(image, height=500, width=450) # you can resize the image

# resolution of image
height = image.shape[1]
width = image.shape[0]
res = width, height

pg.init()
# create the display of the image
surface = pg.display.set_mode(res)
pg.display.set_caption('ASCII Image')

# update these variables - with size, characters, style of your choice
font_size = 6
#ascii_chars = ' .",:;!~+-xmo*#W&8@'
#ascii_chars = " %&//#"
ascii_chars = " ABCDEFGHIJKLMNOPQRSTU"
font_style = "Comic MS Sans"
new_file_name = "flower_3"
background_colour = "orange" # any colour aside from white should work


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    surface.fill(background_colour) # you can also change the background colour
    draw_converted_image(image, ascii_chars, font_style, font_size, surface)
    pg.display.flip()
    # launch the image using cv for comparison
    cv2.imshow("Original image flipped", image)


# save image to a location and name of your choice
save_image(surface, f"image/{new_file_name}.png")
