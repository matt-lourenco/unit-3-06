# Created by: Matthew Lourenco
# Created on 18 Oct 2016
# This program creates a moving image.

from __future__ import division
import ui
import time

walking_man_image = ui.Image.named('./assets/sprites/walk1.bmp')
walkingimageview = ui.ImageView(frame=(70, 40, 180, 180))
walkingimageview.image = walking_man_image

box = ['./assets/sprites/walk1.bmp', './assets/sprites/walk2.bmp', './assets/sprites/walk3.bmp', './assets/sprites/walk4.bmp', './assets/sprites/walk5.bmp', './assets/sprites/walk6.bmp', './assets/sprites/walk7.bmp', './assets/sprites/walk8.bmp', './assets/sprites/walk9.bmp', './assets/sprites/walk10.bmp']

@ui.in_background

def start_touch_up_inside(sender):
    
    count = 0
    
    while True:
        
        if count < 10:
            walking_man_image = ui.Image.named(box[count])
            walkingimageview.image = walking_man_image
            time.sleep(1/15)
            count = count + 1
        else:
            count = 0

view = ui.load_view()
view.add_subview(walkingimageview)
view.present('sheet')
