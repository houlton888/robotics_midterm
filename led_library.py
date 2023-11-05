import time
from machine import Pin

pins = [
    Pin(27,Pin.OUT), #1 top
    Pin(26,Pin.OUT), #3 top right
    Pin(22,Pin.OUT), #4 middle
    Pin(21,Pin.OUT), #5 top right
    Pin(0,Pin.OUT), #6 bottom right
    Pin(1,Pin.OUT), #7 dot
    Pin(3,Pin.OUT), #8 bottom left
    Pin(4,Pin.OUT) #10 bottom
]
left_num = Pin(28,Pin.OUT)
right_num = Pin(2,Pin.OUT)

nums = {
    0:[1,1,1,1,1,1,1,1],
    1:[1,0,1,1,0,1,1,1],
    2:[0,0,0,1,1,1,0,0],
    3:[0,0,0,1,0,1,1,0],
    4:[1,0,0,0,0,1,1,1],
    5:[0,1,0,0,0,1,1,0],
    6:[0,1,0,0,0,1,0,0],
    7:[0,0,1,1,0,1,1,1],
    8:[0,0,0,0,0,1,0,0],
    9:[0,0,0,0,0,1,1,1],
    "f":[0,1,0,0,1,1,0,1],
    "c":[0,1,1,0,1,1,0,0]
}

left_num.value(1)
right_num.value(0)

def led_display(side,value):
    #value is from dict nums, side is either left or right
    if side == "left":
        left_num.value(1)
        right_num.value(0)
    if side == "right":
        left_num.value(0)
        right_num.value(1)
    if side == "off":
        left_num.value(0)
        right_num.value(0)
        
    for j in range(len(pins)):
        pins[j].value(nums[value][j])

led_display("off",4)