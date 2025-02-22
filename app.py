from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import patient_routes, doctor_routes, appointment_routes, vital_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

app.register_blueprint(patient_routes)
app.register_blueprint(doctor_routes)
app.register_blueprint(appointment_routes)
app.register_blueprint(vital_routes)

if __name__ == '__main__':
    app.run(debug=True)
