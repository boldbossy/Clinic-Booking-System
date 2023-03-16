# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# pylint: disable=no-member
# pylint: disable=E1101
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/appointment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/notification', methods=['POST'])
def handle_notification():
    data = request.get_json()
    appointmentID = data.get('appointmentID')
    status = data.get('status')
    email = data.get('email')
    
    # Send email to person with appointment status
    # ...
    if status == "200":
        message = Mail(
            from_email='doctorasap2023@gmail.com',
            to_emails=email,
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>'
        )
    try:

        sg = SendGridAPIClient(os.environ.get('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'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
    
    return jsonify({'message': 'Notification received'})