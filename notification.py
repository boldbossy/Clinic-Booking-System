import os
import json

import amqp_setup

import os
from twilio.rest import Client

monitorBindingKey='#'

def receiveNotification():
    amqp_setup.check_setup()
    
    queue_name = "Notification"  

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 

def handle_notification(body):
    appointment = json.loads(body)
    if 'data' in appointment:
        data = appointment['data']
        mobile = data['mobile']
        appointmentID = data['appointmentID']
        name = data['name']
        datetime = data['datetime']
        status = appointment['code']
        account_sid = "ACefec66bc804dfb402d99d144b257f64b"
        auth_token = "02f493127c4a7191f1e1ba166af0129f"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body= f"Hello {name}, your appointment on {datetime} is confirmed. Your appointment ID is {appointmentID}.",
        from_="+15076691400",
        to = f"{mobile}",)

        print(message.sid)

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="notification", body=json.dumps({
                                            "appointmentID": appointmentID,
                                            "mobile": mobile,
                                            "name": name,
                                            "status": status
                                        }))

def callback(channel, method, properties, body):
    print("\nReceived an notification from " + __file__)
    # if status == '200':
    handle_notification(body)
    print()

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')    
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveNotification()