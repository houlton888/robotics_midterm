import requests
import json
id = "app2KIcVxkpobiLVn"
AIRTABLE_URL = f"https://api.airtable.com/v0/{id}"
AIRTABLE_TOKEN = "patjLrrA8634AGtXB.3ef57f68408bb2e18092db5983dad27885a7a4a74ac80d5ee1d8b6b186be5c3c"
url = f"{AIRTABLE_URL}/Table"
headers = {
    'Authorization': 'Bearer ' + str(AIRTABLE_TOKEN),
    'Content-Type': 'application/json',
    }
blue = {
    "records": [
        {
            "fields": {
                "color": "blue",
            }
        }
    ]
}
green = {
    "records": [
        {
            "fields": {
                "color": "green",
            }
        }
    ]
}
red = {
    "records": [
        {
            "fields": {
                "color": "red",
            }
        }
    ]
}

#cam.snap()
cv2_image = cv2.cvtColor(np.array(cam.raw_image), cv2.COLOR_RGB2BGR)
cv2_copy = cv2_image
cv2_copy[:,:,0], cv2_copy[:,:,1], cv2_copy[:,:,2] = np.average(cv2_copy, axis=(0,1)) # makes image into average color
r_ave = cv2_copy[0,0,2] #average value of red/green/blue in the image
g_ave = cv2_copy[0,0,1]
b_ave = cv2_copy[0,0,0]
print(cv2_copy[0,0,:])
color = ''
if r_ave > g_ave and r_ave > b_ave:
    color = red
if g_ave > r_ave and g_ave > b_ave:
    color = green
if b_ave > r_ave and b_ave > g_ave:
    color = blue

cam.show(cv2_copy)  # shows any cv2 image in the same spot on the webpage (third image)
response = requests.request("POST", url, headers=headers, data=json.dumps(color))