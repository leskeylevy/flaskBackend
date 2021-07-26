from .. import db
import datetime


class Comments(db.Model):
    """ Comments model for storing blog comments"""
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(700), nullable=False)
    blog_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    likes = db.Column(db.Integer, autoincrement=True)
    dislikes = db.Column(db.Integer, autoincrement=True)

    def __repr__(self):
        return "<Comment '{}'>".format(self.comment)
