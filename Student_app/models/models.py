
from Student_app import db

class Student(db.Model):
    __tablename__="students"

    Name=db.Column(db.String(25))
    Mobile=db.Column(db.Integer, primary_key=True)
    Address=db.Column(db.String(40))
    Education=db.Column(db.String(30))


    def save(self):
        db.session.add(self)
        db.session.commit()

