from flask import Flask,request
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('C:\\sharath\projects\\assignments\\week 7\\week7.h5')
model.summary()

label_names = {    
0 : 'airplane',										
1 : 'automobile',										
2 : 'bird',										
3 : 'cat',										
4 : 'deer',										
5 : 'dog',										
6 : 'frog',
7 : 'horse',										
8 : 'ship',										
9 : 'truck',
}

app = Flask(__name__)
@app.route('/') 
def welcome():
  return 'hello'
@app.route('/pred',methods = ['POST','GET'])
def serve_model():
    
    request_data = request.get_json(force=True)
    img = request_data['img']
    img = np.array(img)
    return ('The prediction is {}'.format(label_names[model.predict(img).argmax()]))

if __name__ == '__main__':
  app.run()
