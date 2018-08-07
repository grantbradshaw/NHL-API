from app import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contracts = db.relationship('Contract', backref='player', lazy=True)

    def __init__(self, name, contracts):
        self.name = name
        self.contracts = contracts

    def __repr__(self):
        return '<id {}>'.format(self.id)