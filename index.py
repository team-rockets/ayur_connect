import flask
import requests

# Create the application.
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')
    ''''def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
        'apikey':'xxxxxxxxxxxxxxxxxxxxxxxxx',
        'secret':'xxxxxxxxxxxxxxxxxxxxxx',
        'usetype':'stage',
        'phone':'xxxxxxxxxxxx',
        'message':'OTP is 4898' ,
        'senderid':'xxxxxxxxxxxx'
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
