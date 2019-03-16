import pyrebase
from flask import *
app=flask.Flask(__name__)
config= {
     "apiKey": "AIzaSyDkjNXBrYHIVC-PGlyAYCuNEx9KIssRgVU",
    "authDomain": "ayur-7ec86.firebaseapp.com",
    "databaseURL": "https://ayur-7ec86.firebaseio.com",
    "projectId": "ayur-7ec86",
    "storageBucket": "ayur-7ec86.appspot.com",
    "messagingSenderId": "678410598979" 
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
email= input('Enter Email')
password = input('Password')
#user = auth.create_user_with_email_and_password(email, password)
auth.send_email_verification(user['idToken'])
user = auth.sign_in_with_email_and_password
#user = auth.get_account_info(user['idToken'])

auth.send_password_reset_email(user['idToken'])


@app.route('/patient_auth',methods=['GET','POST'])
def sign():
    unsuccesful = 'Please check credentials'
    if request.method == 'POST' :
        mr = request.form['mrno']
        try:
            auth.sign_in_with_email_and_password(mrno,password)
            return 'Success'
        except:
            return render_template('op.html', us=unsuccesful)
    return render_template('op.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run()
