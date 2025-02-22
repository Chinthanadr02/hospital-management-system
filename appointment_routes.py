from flask import Blueprint, request, jsonify
from models import db, Appointment

appointment_routes = Blueprint('appointment_routes', __name__)

@appointment_routes.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments])

@appointment_routes.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    return jsonify(appointment.to_dict())

@appointment_routes.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    new_appointment = Appointment(patient_id=data['patient_id'], doctor_id=data['doctor_id'], appointment_date=data['appointment_date'], status=data['status'])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

@appointment_routes.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    data = request.get_json()
    appointment = Appointment.query.get_or_404(id)
    appointment.patient_id = data['patient_id']
    appointment.doctor_id = data['doctor_id']
    appointment.appointment_date = data['appointment_date']
    appointment.status = data['status']
    db.session.commit()
    return jsonify(appointment.to_dict())

@appointment_routes.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return '', 204
