import numpy as np
import requests
import json
from tensorflow.keras.preprocessing.image import load_img

img = np.array(load_img('C:\\sharath\\projects\\assignments\\week 7\\horse.png'))
img.resize(1,32,32,3)

img = img.tolist()

url = ' http://localhost:5000/pred'
requested_data = json.dumps({'img':img})
headers = {
 'content-type':'application/json'
}

response = requests.post(url,data = requested_data,headers = headers)

print(response.text )
