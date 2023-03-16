from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
 
db = SQLAlchemy(app)
CORS(app)

 
class Clinic(db.Model):
    __tablename__ = 'clinic'
 
    clinicID = db.Column(db.Integer, nullable=False)
    clinicName = db.Column(db.String(64), primary_key=True)
    clinicLoc = db.Column(db.String(64), nullable=False)
    waitTime = db.Column(db.TIME, nullable=False)
 
    def __init__(self, clinicID, clinicName, clinicLoc, waitTime):
        self.clinicID = clinicID
        self.clinicName = clinicName
        self.clinicLoc = clinicLoc
        self.waitTime = waitTime
 
    def json(self):
        to = {
            'clinicID': self.clinicID, 
            'clinicName': self.clinicName, 
            'clinicLoc': self.clinicLoc, 
            'waitTime': str(self.waitTime)
        }
        return to

@app.route("/clinic")
def get_all():
    cliniclist = Clinic.query.all()
    if len(cliniclist):
        return(
            {
                "code": 200,
                "data": {
                    "clinics": [clinic.json() for clinic in cliniclist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no clinics."
        }
    ), 404

 
@app.route("/clinic/<string:clinicName>")
def find_by_clinicLoc(clinicName):
    clinic = Clinic.query.filter_by(clinicName=clinicName).first()
    if clinic:
        return jsonify(
            {
                "code": 200,
                "data": clinic.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Clinic not found."
        }
    ), 444

 
@app.route("/clinic/<string:clinicName>", methods=['POST'])
def create_clinic(clinicName):
    if (Clinic.query.filter_by(clinicName=clinicName).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "clinicName": clinicName
                },
                "message": "Clinic already exists."
            }
        ), 400
 
    data = request.get_json()
    clinic = Clinic(clinicName, **data)
 
    try:
        db.session.add(clinic)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "clinicName": clinicName
                },
                "message": "An error occurred creating the clinic."
            }
        ), 500
        
 
    return jsonify(
        {
            "code": 201,
            "data": clinic.json()
        }
        ), 201

 
if __name__ == '__main__':
    app.run(port=5000, debug=True)
