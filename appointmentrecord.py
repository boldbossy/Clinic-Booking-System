from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/appointment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Appointment(db.Model):
    __tablename__ = 'appointment'

    appointmentID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    clinicName = db.Column(db.String(64), primary_key=True, nullable=False)
    nric = db.Column(db.String(9), nullable=False)
    mobile = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __init__(self, clinicName, nric, mobile, name, address, dob, datetime):
        self.clinicName = clinicName
        self.nric = nric
        self.mobile = mobile
        self.name = name
        self.address = address
        self.dob = dob
        self.datetime = datetime

    def json(self):
        return {"appointmentID": self.appointmentID, "clinicName": self.clinicName, "nric": self.nric, "mobile": self.mobile, "name": self.name, "address": self.address, "dob": datetime.strftime(self.dob, '%Y-%m-%d'), "datetime": self.datetime}
    

@app.route("/appointment")
def get_all_appointments():
    appointment_list = Appointment.query.all()
    if len(appointment_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "appointments": [appointment.json() for appointment in appointment_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no appointments."
        }
    ), 404

@app.route('/appointment/<int:appointmentID>', methods=['GET'])
def find_by_appointment(appointmentID):
    appointment = Appointment.query.filter_by(appointmentID=appointmentID).first()
    if appointment:
        return jsonify(
            {
                "code": 200,
                "data": appointment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Appointment not found."
        }
    ), 404

@app.route('/appointment/<string:nric>', methods=['GET'])
def find_by_nric(nric):
    appointment = Appointment.query.filter_by(nric=nric).first()
    if appointment:
        return jsonify(
            {
                "code": 200,
                "data": appointment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"Appointment under customer {nric} not found."
        }
    ), 404

@app.route("/appointment/<string:clinicName>")
def find_by_clinicName(clinicName):
    appointment_list = Appointment.query.filter_by(clinicName=clinicName).all() # .first returns 1 book instead of a list of all the books
    if appointment_list:
        return jsonify(
            {
                "code": 200, # even if you change this to any other number e.g. 216, the status will still be 200 OK, even though it will print "code": 216
                "data": [appointment.json() for appointment in appointment_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Appointment in clinic chosen not found."
        }
    ), 404

@app.route('/appointment/<string:clinicName>', methods=['POST'])
def create_appointment(clinicName):
    
    data = request.get_json()

    # Check for overlapping appointments
    posted_datetime = datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
    existing_appointments = Appointment.query.filter_by(clinicName=clinicName).all()
    for appt in existing_appointments:
        if appt.datetime <= posted_datetime < appt.datetime + timedelta(minutes=15):
            return jsonify({
                "code": 400,
                "message": "There is already an existing appointment at this time."
            }), 400
        
    # CHECK FOR MULTIPLE APPOINTMENTS ON SAME DAY FOR SAME CUSTOMER
    nric = data['nric']
    appt_date = posted_datetime.date()
    existing_appts = Appointment.query.filter_by(nric=nric).all()
    for appt in existing_appts:
        if appt.datetime.date() == appt_date:
            return jsonify({
                "code": 400,
                "message": "You already have an appointment on this date."
            }), 400

        
    appointment = Appointment(
        # appointmentID=data['appointmentID'],
        clinicName=clinicName,
        nric=data['nric'],
        mobile=data['mobile'],
        name=data['name'],
        address=data['address'],
        dob=data['dob'],
        datetime=datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
    )

    try:
        db.session.add(appointment)
        db.session.commit()
        # app.logger.info(appointment.appointmentID)

    except:
        return jsonify({
            "code": 500,
            "data": {
                "appointmentID": appointment.appointmentID,
                "clinicName": clinicName
            },
            "message": "An error occurred creating the appointment."
        }), 500
    
    return jsonify({
        "code": 201,
        "data": {
            "appointmentID": appointment.appointmentID,
            "clinicName": appointment.clinicName,
            "nric": appointment.nric,
            "mobile": appointment.mobile,
            "name": appointment.name,
            "address": appointment.address,
            "dob": appointment.dob,
            "datetime": appointment.datetime.strftime('%Y-%m-%d %H:%M:%S')
        }
    }), 201

@app.route('/appointment/<int:appointmentID>', methods=['DELETE'])
def delete_appointment(appointmentID):
    appointment = Appointment.query.filter_by(appointmentID=appointmentID).first()
    if not appointment:
        return jsonify({
            "code": 404,
            "message": "Appointment not found."
        }), 404

    try:
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({
            "code": 200,
            "message": "Appointment deleted successfully."
        }), 200

    except:
        return jsonify({
            "code": 500,
            "message": "An error occurred deleting the appointment."
        }), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)