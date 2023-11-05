import time
from machine import Pin, PWM

pins = {
    0:27,
    1:26,
    2:22,
    3:21,
    4:0,
    5:3,
    6:4
}

pulse = {
    0:4,
    1:999
}

nums = {
    0:[0,0,1,0,0,1,0,0],
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
    "c":[0,1,1,0,1,1,0,0],
    "dot":[1,1,1,1,1,0,1,1],
    "off":[1,1,1,1,1,1,1,1]
}

PWM.setup()
PWM.init_channel(0)
PWM.add_channel_pulse(0,28,0,999)
PWM.add_channel_pulse(0,2,1000,999)


def pwm_num(value):
    digits = map(int, "%02d" % value)
    
    for i in range(7):
        PWM.add_channel_pulse(0,pins[i],0,num[digits[0][i]])
        PWM.add_channel_pulse(0,pins[i],1000,num[digits[1][i]])
        
pwm_num(25)
