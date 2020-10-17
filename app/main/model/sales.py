from .. import db


class SoldProducts(db.Model):
    """ Model for storing sold product and related details"""
    __tablename__ = "soldProducts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    productCode = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    sold_on = db.Column(db.DateTime, nullable=False)
    supplierId = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_phone_number = db.Column(db.String(100), nullable=False)
    mpesa_transaction_code = db.Column(db.String(100), nullable=False)
    order_number = db.Column(db.String(100), nullable=False)
    delivery_status = db.Column(db.String(50), nullable=False, default='Pending')

    def __repr__(self):
        return "<Sold product '{}'>".format(self.name)
