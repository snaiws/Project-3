from p3_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class corp_model(db.Model):
    __tablename__ = 'corp'

    id = db.Column(db.Integer(),primary_key=True)
    corp_code = db.Column(db.Integer(),ForeignKey('key_model.corp_code'))
    corp_name = db.Column(db.String())
    ind_code = db.Column(db.Integer())
        

    corp_codes=relationship('key_model',back_populates='corps')
    inds=relationship('ind_model',back_populates='ind_codes')
    

    def __repr__(self):
        return dict(corp_code = self.corp_code, corp_name = self.corp_name, ind_code = self.ind_code)