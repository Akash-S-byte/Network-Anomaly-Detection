from flask import Flask, request, jsonify

import pickle

import pandas as pd


app = Flask(__name__)

# Load encoders and model
with open('./network_anomaly_detection_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
with open('./one_hot_encoding.pkl', 'rb') as file:
    one_hot_encoder = pickle.load(file)
with open('./service_freq_encoding.pkl', 'rb') as file:
    service_freq_encoder = pickle.load(file)
with open('./flag_freq_encoding.pkl', 'rb') as file:
    flag_freq_encoder = pickle.load(file)
with open('./scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def welcome_note():
    return "<h1>Network Anomaly Classification App</h1>"


# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from POST request
    data = request.get_json()


    #Apply one-hot-encoding to 'protocoltype'
    if data['protocoltype']=='tcp':
        data['protocoltype_tcp'] = 1.0
        data['protocoltype_udp'] = 0.0
        data['protocoltype_icmp'] = 0.0
    elif data['protocoltype']=='udp':
        data['protocoltype_tcp'] = 0.0
        data['protocoltype_udp'] = 1.0
        data['protocoltype_icmp'] = 0.0
    elif data['protocoltype']=='icmp':
        data['protocoltype_tcp'] = 0.0
        data['protocoltype_udp'] = 0.0
        data['protocoltype_icmp'] = 1.0


    # Convert data to DataFrame
    df = pd.DataFrame([data])

    df = df.drop('protocoltype', axis=1)
    df = df.drop('dstbytes', axis=1)    

    # Apply frequency encoding to 'service'
    df['service_encoded'] = df['service'].map(service_freq_encoder)
    df =df.drop('service', axis=1)
    
    # Apply frequency encoding to 'flag'
    df['flag_freq_encoded'] = df['flag'].map(flag_freq_encoder)
    df =df.drop('flag', axis=1)

    # Predict using the model
    prediction = loaded_model.predict(df)
    return jsonify({'prediction': int(prediction[0])})
   
if __name__ == "__main__":
    app.run(debug = True)