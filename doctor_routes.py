from flask import Blueprint, request, jsonify
from models import db, Doctor

doctor_routes = Blueprint('doctor_routes', __name__)

@doctor_routes.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctor.to_dict() for doctor in doctors])

@doctor_routes.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    return jsonify(doctor.to_dict())

@doctor_routes.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()
    new_doctor = Doctor(name=data['name'], specialization=data['specialization'], contact_info=data['contact_info'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(new_doctor.to_dict()), 201

@doctor_routes.route('/doctors/<int:id>', methods=['PUT'])
def update_doctor(id):
    data = request.get_json()
    doctor = Doctor.query.get_or_404(id)
    doctor.name = data['name']
    doctor.specialization = data['specialization']
    doctor.contact_info = data['contact_info']
    db.session.commit()
    return jsonify(doctor.to_dict())

@doctor_routes.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    doctor = Doctor.query.get_or_404(id)
    db.session.delete(doctor)
    db.session.commit()
    return '', 204
