import uuid
import datetime

from app.main import db
from app.main.model.comments import Comments


def save_new_comment(data):
    comnt = Comments.query.filter_by(comment=data['comment']).first()
    if not comnt:
        new_comment = Comments(
            username=data['username'],
            comment=data['comment'],
            blog_id=data['blog_id']
        )
        save_comment(new_comment)
        response_object = {
            'status': 'success',
            'message': 'Comment successfuly added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Comment already exists!'
        }
        return response_object, 409


def get_all_comments(blog_id):
    return Comments.query.filter_by(blog_id=blog_id).all()


def save_comment(data):
    db.session.add(data)
    db.session.commit()
