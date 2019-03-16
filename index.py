import flask
import requests

# Create the application.
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')
    ''''def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
        'apikey':'EJNDMSDX8B6M48NCT43L5Q5MXW4SKIH4',
        'secret':'YSXVIV4B6FVW7LLT',
        'usetype':'stage',
        'phone': '7012161270',
        'message':'OTP is 4898' ,
        'senderid':'Rizwan'
        }
        return requests.post(reqUrl, req_params)'''

   
        

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(output)


if __name__ == '__main__':
    app.debug=True
    app.run()
