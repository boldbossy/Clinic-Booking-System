# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# pylint: disable=no-member
# pylint: disable=E1101
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from app import views, models
import requests

import amqp_setup
import pika

monitorBindingKey='#'

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/notification'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# @app.route('/notification', methods=['POST'])

def receiveNotification():
    amqp_setup.check_setup()
    
    queue_name = "Notification"  

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def handle_notification(appointmentID, status, email):
    content = request.get_json()
    appointmentID = content.get('appointmentID')
    status = content.get('status')
    email = content.get('email')
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

# def connect_to_rabbitmq():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
#     channel = connection.channel()
#     channel.queue_declare(queue='notification_queue')
#     return channel

def callback(channel, method, properties, body):
    # with app.app_context():
    data = json.loads(body)
    appointmentID = data.get('appointmentID')
    status = data.get('status')
    email = data.get('email')
    print("\nReceived an notification from " + __file__)
    # if status == '200':
    handle_notification(appointmentID, status, email)
    print()

def processNotification(notification):
    print("Recording a notification:")
    print(notification)

# channel = connect_to_rabbitmq()
# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(queue='notification_queue', on_message_callback=callback)
# channel.start_consuming()   

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')    
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveNotification()