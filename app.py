from flask import Flask, jsonify, request
import pickle
import numpy as np


app = Flask(__name__)

with open('model_jebin','rb') as f:

    model = pickle.load(f)

@app.route('/')
def home():
    return "Hello world"


@app.route('/predict',methods = ['POST'])

def predict():
    happy = request.form.get('happy')
    sad = request.form.get('sad')
    apetite = request.form.get('apetite')
    stress = request.form.get('stress')
   
    ratings = [happy,sad,apetite,stress]
    b = np.array(ratings, dtype=float)
    
    input_data = (b)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    result = model.predict(input_data_reshaped)[0]

    if result == 1:
        return jsonify({'mood': str('good')})
    else:
        return jsonify({'mood': str('bad')})


# class getEmotion(Resource):
  
    
#     def post(self):
          
#         data = request.get_json()     # status code
#         return jsonify({'data': data}), 201
  
  
# # adding the defined resources along with their corresponding urls
# api.add_resource(getEmotion, '/')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)