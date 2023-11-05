import libraries.othmro_led_lib as led
import Codes.airtable as key
from libraries import Accel_lib_sarvey as accel
from machine import Pin, PWM
import time
from libraries import mqtt
import math
import urequests as requests
import json
import Codes.secrets as codes

#connect to wifi
codes.connect_wifi(codes.Home_Wifi)

#set up accelerometer
acc = accel.accelerometer(0,1,0)
analog_value = machine.ADC(28)
acc_init_val = acc.read_a()[2]

#connect to adafruit mqtt
ADAFRUIT_IO_KEY = codes.io_key
ADAFRUIT_IO_USERNAME = codes.io_username
def whenCalled(topic, msg):
    print((topic.decode(), msg.decode()))
client1 = mqtt.MQTTClient("temp_unit",'io.adafruit.com',user=ADAFRUIT_IO_USERNAME, password=ADAFRUIT_IO_KEY)
client1.connect()
client1.set_callback(whenCalled)
client2 = mqtt.MQTTClient("temp_reading",'io.adafruit.com',user=ADAFRUIT_IO_USERNAME, password=ADAFRUIT_IO_KEY)
client2.connect()
client2.set_callback(whenCalled)

#set up airtable api connection
id = "app2KIcVxkpobiLVn"
AIRTABLE_URL = f"https://api.airtable.com/v0/{id}"
TOKEN = key.AIRTABLE_TOKEN
url = f"{AIRTABLE_URL}/Table"
headers = {
    'Authorization': 'Bearer ' + str(TOKEN),
    'Content-Type': 'application/json',
    }
def get_data():
    global url
    global headers
    response = requests.get(url, headers = headers)
    return response

#Waits for accelerometer to be moved and then reads and dislpays temperature and sends to adafruit mqtt      
while True:
    acc_val = acc.read_a()[2]
    if acc_val - acc_init_val > 1000: #if breadboard tilted
        print("accel triggered")
        #find temp
        ADC = analog_value.read_u16()
        ADC = float(ADC)
        R = 655/(ADC/1000) - 10 
        Kelv = 1/((1/295)+(1/3950)*math.log(R/10.9)) #https://www.eaa.net.au/PDF/Hitech/MF52type.pdf for B val
        fahr_temp = (Kelv - 273.15)*(9/5)+32
        #get color from airtable
        table = get_data()
        records = table.json()['records']
        last_record = records[len(records)-1]
        color = last_record['fields']['color']
        temp_unit = "f"
        tempf = fahr_temp
        if color == "blue":
            temp_unit = "c"
            tempf = (tempf - 32) * (5/9)
        if color == "red":
            temp_unit = "c"
            tempf = (tempf - 32) * (5/9)
        #print to display
        temp = led.split_num(tempf)
        led.display(3,temp[0],temp[1],temp_unit) #displays temp for 3 seconds
        #send over mqtt to adafruit
        client1.publish('houlton888/feeds/robotics-midterm.unit-of-temperature',temp_unit)
        client1.publish('houlton888/feeds/robotics-midterm.temperature',str(tempf))
        time.sleep(5)
 

