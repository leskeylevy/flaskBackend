from .. import db
from slugify import slugify


class Blog(db.Model):
    """ Blog model for storing blog related details"""
    __tablename__ = "blog_post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    slug = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(120000), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    caption = db.Column(db.String(5000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    author_id = db.Column(db.Integer)
    updated_on = db.Column(db.DateTime, nullable=False)

    def slugify_title(self, title):
        self.slug = slugify(title)

    def __repr__(self):
        return "<Blog '{}' > ".format(self.title)
