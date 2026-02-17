from .dbconnection import db

class DealsItems(db.Model):
    __tablename__ = "deals_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer)

    # test