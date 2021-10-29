from flask import Flask, json, request, jsonify
import util

app= Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response= jsonify({
        'locations': util.get_location_names()
    }) 
    response.headers.add('Access-control-Allow-origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqrt= float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqrt, bhk, bath)
    })

    return response 

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.get_saved_artifacts()
    app.run()  