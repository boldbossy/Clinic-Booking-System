from invokes import invoke_http

# invoke book microservice to get all books
results = invoke_http("http://127.0.0.1:5000/appointment", method='GET')

print( type(results) )
print()
print( results )

# invoke appointment_record microservice to create an appointment
appointmentID = 5
clinicName = 'Complete Hospital International'
appointment_details = {
            "appointmentID" : 5,
            "clinicName": "Complete Hospital International",
            "datetime": "2022-07-02 10:45:30",
            "name": "Margaret Lim",
            "email": "doctorasap2023@gmail.com",
            "address": "170 UPPER BUKIT TIMAH ROAD",
            "dob": "1996-10-10",
            "nric": "S9650951A"
        }
create_results = invoke_http(
        "http://127.0.0.1:5000/appointment/" + str(appointmentID) + "/" + clinicName, method='POST', 
        json=appointment_details
    )

print()
print( create_results )
