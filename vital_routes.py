from flask import Blueprint, request, jsonify
from models import db, Vital

vital_routes = Blueprint('vital_routes', __name__)

@vital_routes.route('/vitals', methods=['GET'])
def get_vitals():
    vitals = Vital.query.all()
    return jsonify([vital.to_dict() for vital in vitals])

@vital_routes.route('/vitals/<int:id>', methods=['GET'])
def get_vital(id):
    vital = Vital.query.get_or_404(id)
    return jsonify(vital.to_dict())

@vital_routes.route('/vitals', methods=['POST'])
def create_vital():
    data = request.get_json()
    new_vital = Vital(patient_id=data['patient_id'], bp=data['bp'], temperature=data['temperature'], date_recorded=data['date_recorded'])
    db.session.add(new_vital)
    db.session.commit()
    return jsonify(new_vital.to_dict()), 201

@vital_routes.route('/vitals/<int:id>', methods=['PUT'])
def update_vital(id):
    data = request.get_json()
    vital = Vital.query.get_or_404(id)
    vital.patient_id = data['patient_id']
    vital.bp = data['bp']
    vital.temperature = data['temperature']
    vital.date_recorded = data['date_recorded']
    db.session.commit()
    return jsonify(vital.to_dict())

@vital_routes.route('/vitals/<int:id>', methods=['DELETE'])
def delete_vital(id):
    vital = Vital.query.get_or_404(id)
    db.session.delete(vital)
    db.session.commit()
    return '', 204
