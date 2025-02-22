from flask import Blueprint, request, jsonify
from models import db, Patient

patient_routes = Blueprint('patient_routes', __name__)

@patient_routes.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@patient_routes.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient.to_dict())

@patient_routes.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], date_of_birth=data['date_of_birth'], contact_info=data['contact_info'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(new_patient.to_dict()), 201

@patient_routes.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    patient = Patient.query.get_or_404(id)
    patient.name = data['name']
    patient.date_of_birth = data['date_of_birth']
    patient.contact_info = data['contact_info']
    db.session.commit()
    return jsonify(patient.to_dict())

@patient_routes.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204
