from p3_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class key_model(db.Model):
    __tablename__ = 'key'

    id = db.Column(db.Integer(),primary_key=True)
    corp_code = db.Column(db.Integer())
    corp_name = db.Column(db.String())

    corps=relationship('corp_model', back_populates='keys')

    def __repr__(self):
        return dict(corp_code = self.corp_code, corp_name = self.corp_name)