import pygame as pg
pg.init()

animations = {"animation": []}
sprite_frame_number = 18

img = pg.Surface((1440, 80))  # that would be the sprite sheet
size = [int(img.get_width() / sprite_frame_number), img.get_height()]  # so in this case size = [80,80]

for x in range(sprite_frame_number):
    frame_location = [size[0] * x, 0]  # so starting with 0, x moves with each iteration 80 pxl to the right
    img_rect = pg.Rect(frame_location, size)
    
    new_img = img.subsurface(img_rect)  # not the same variable as img
    animations["animation"].append(new_img)
    
print(animations)