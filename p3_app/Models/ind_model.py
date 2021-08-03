from p3_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ind_model(db.Model):
    __tablename__ = 'ind'

    id = db.Column(db.Integer(),primary_key=True)
    ind_code = db.Column(db.Integer(),ForeignKey('corp_model.ind_code'))
    iClass1= db.Column(db.String())
    iClass2= db.Column(db.String())
    iClass3= db.Column(db.String())
    iClass4= db.Column(db.String())
    iClass5= db.Column(db.String())
    ind_codes=relationship('corp_model',back_populates='inds')
    

    def __repr__(self):
        return dict(ind_code = self.ind_code, iClass1 = self.iClass1, iClass2 = self.iClass2, iClass3 = self.iClass3, iClass4= self.iClass4, iClass5 = self.iClass5)
