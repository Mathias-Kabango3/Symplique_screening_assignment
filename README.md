Remind-me-later API
This API allows clients to store reminder messages with a scheduled date/time and a delivery method (SMS or Email). It's designed to be used by a frontend to collect reminder data from users and save it to the database.

Features
Accepts message, date, time, and reminder method

Stores data in  SQLite database

Supports email and sms (extensible for more)

Installation
# Clone the project
git clone https://github.com/Mathias-Kabango3/Symplique_screening_assignment
cd remindme

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
API Endpoint
POST /api/reminders/
Creates a new reminder.

Request Body (JSON)
{
  "date": "2025-06-08",
  "time": "14:45:00",
  "message": "Call my doctor",
  "method": "sms"
}
Field	Type	Required	Description
date	string	✅	Date for the reminder (YYYY-MM-DD)
time	string	✅	Time for the reminder (HH:MM:SS)
message	string	✅	Reminder text/message
method	string	✅	"sms" or "email"

✅ Example Success Response
Status: 201 Created

{
  "id": 1,
  "status": "created"
}
❌ Example Error Response
Status: 400 Bad Request

{
  "non_field_errors": [
    "Remind time must be in the future."
  ]
}
Testing the API
Use curl or Postman to test:

curl -X POST http://127.0.0.1:8000/api/reminders/ 
  -H "Content-Type: application/json" 
  -d '{
    "date": "2025-06-08",
    "time": "10:00:00",
    "message": "Submit assignment",
    "method": "email"
  }'


Project Structure
remindme/
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── remindme/
│   └── settings.py
├── manage.py
└── requirements.txt

Author
Built for a screening assignment by Mathias Kabango.

