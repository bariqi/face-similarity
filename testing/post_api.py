import requests
import cv2
import base64
import datetime

image = cv2.imread('data\\person1a.jpeg')
# image = cv2.imread('data\\person2a.jpg')
ret, buffer = cv2.imencode('.jpg', image)
jpg_as_text1 = base64.b64encode(buffer).decode('utf-8')

image2 = cv2.imread('data\\person2b.jpg')
ret2, buffer2 = cv2.imencode('.jpg', image2)
jpg_as_text2 = base64.b64encode(buffer2).decode('utf-8')

data = {
  "photo1": jpg_as_text1,
  "photo2": jpg_as_text2
}

# url = 'http://10.48.103.139:8000/detectandrecog'
url = 'http://localhost:8000/verify'
response = requests.post(url, json=data)
print(response.text)