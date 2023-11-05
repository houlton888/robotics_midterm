# robotics_midterm
Sources Used:
https://learn.adafruit.com/lsm6dsox-and-ism330dhc-6-dof-imu/arduino
https://airtable.com/developers/web/guides/personal-access-tokens
https://www.w3schools.com/python/gloss_python_if_and.asp
https://www.amazon.com/gp/product/B0166I8IU8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.digikey.com/en/products/detail/ametherm/1DC103J-EC/5970120?utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_High%20ROAS%20Categories&utm_term=&utm_content=&gclid=CjwKCAjw7oeqBhBwEiwALyHLM3nyGihO57Vmf9OXTLkxDw61hVebdcIxANpwSAjgHwGrup11aS1sbxoC7CgQAvD_BwE
https://www.northstarsensors.com/calculating-temperature-from-resistance
https://dev.to/matthewvielkind/using-python-and-airtable-3bb7
https://hevodata.com/learn/airtable-python/
https://blog.futuresmart.ai/mastering-airtable-rest-api-with-python-a-step-by-step-guide

List to OpenCV Website:
https://chrisrogers.pyscriptapps.com/me35-midterm/latest/

Library Structure:
main code on pico uses following libraries:
1) othmro_led_lib:
   -This library defines which pins should be turned on for the LED display to display what numbers/symbols, and makes functions for the user to drive the display easily
3) Codes.airtable
   -has personal authentification token for airtable api stored
5) Accel_lib_sarvey
   -library that makes a class called accel, which makes reading acceleration vslues from an accelerometer into one easy function
7) mqtt
   -library sets up mqtt
9) secrets
   -contatins wifi passwords and connection functions
