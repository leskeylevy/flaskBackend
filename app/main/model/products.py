from .. import db


class Products(db.Model):
    """ Product model for storing product related details"""
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(12000), nullable=False)
    price = db.Column(db.Integer, default=2500, nullable=False)
    added_on = db.Column(db.DateTime, nullable=False)
    productId = db.Column(db.String(100), unique=True)
    supplierId = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    mainImage = db.Column(db.String(100), nullable=False)
    angle1 = db.Column(db.String(100), nullable=False)
    angle2 = db.Column(db.String(100), nullable=True)
    angle3 = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return "<Product '{}'>".format(self.name)
