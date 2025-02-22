from flask import Blueprint

# Initialize Blueprints
patient_routes = Blueprint('patient_routes', __name__)
doctor_routes = Blueprint('doctor_routes', __name__)
appointment_routes = Blueprint('appointment_routes', __name__)
vital_routes = Blueprint('vital_routes', __name__)

# Import the route files to register the routes
from .patient_routes import patient_routes
from .doctor_routes import doctor_routes
from .appointment_routes import appointment_routes
from .vital_routes import vital_routes
