from sqlalchemy.orm import backref
from p3_app import db

class Key_model(db.Model):
    __tablename__ = 'key_model'
    corp_code = db.Column(db.Integer,nullable=False,primary_key=True)
    corp_name = db.Column(db.String(),nullable=False)

    corps=db.relationship('Corp_model', backref='key_model', lazy=True)

    def __repr__(self):
        return dict(corp_code = self.corp_code, corp_name = self.corp_name)

class Corp_model(db.Model):
    __tablename__ = 'corp_model'
    corp_code = db.Column(db.Integer,db.ForeignKey('key_model.corp_code'),nullable=False)
    corp_name = db.Column(db.String(),nullable=False)
    ind_code = db.Column(db.Integer,nullable=False,primary_key=True)
        
    inds=db.relationship('Ind_model',backref='corp_model',lazy=True)
    

    def __repr__(self):
        return dict(corp_code = self.corp_code, corp_name = self.corp_name, ind_code = self.ind_code)

class Ind_model(db.Model):
    __tablename__ = 'ind_model'
    id = db.Column(db.Integer,primary_key=True)
    ind_code = db.Column(db.Integer,db.ForeignKey('corp_model.ind_code'),nullable=False)
    iClass1= db.Column(db.String(),nullable=False)
    iClass2= db.Column(db.String())
    iClass3= db.Column(db.String())
    iClass4= db.Column(db.String())
    iClass5= db.Column(db.String())

    

    def __repr__(self):
        return dict(ind_code = self.ind_code, iClass1 = self.iClass1, iClass2 = self.iClass2, iClass3 = self.iClass3, iClass4= self.iClass4, iClass5 = self.iClass5)
