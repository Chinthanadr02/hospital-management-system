from . import db
from datetime import datetime

class Vital(db.Model):
    __tablename__ = 'vitals'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    bp = db.Column(db.String(10), nullable=False)  # Blood Pressure
    temperature = db.Column(db.Float, nullable=False)
    date_recorded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'bp': self.bp,
            'temperature': self.temperature,
            'date_recorded': self.date_recorded.isoformat()
        }
