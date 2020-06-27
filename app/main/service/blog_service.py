import datetime

from app.main import db
from app.main.model.blog import Blog


def save_new_blog(data):
    blog = Blog.query.filter_by(title=data['title']).first()
    if not blog:
        new_blog = Blog(
            title=data['title'],
            content=data['content'],
            created_on=datetime.datetime.utcnow(),
            status=data['status'],
            caption=data['caption'],
            img=data['img'],
            author_id=data['author']
        )
        save_blog(new_blog)
        response_object = {
            "status": 'Success',
            "message": 'Successfuly added blog'
        }
        return response_object, 201
    else:
        blog.title = data['title']
        blog.content = data['content']
        blog.status = data['status']
        blog.update_on = datetime.datetime.utcnow()
        db.session.commit()

        response_object = {
            'message': "Successfuly edited content",
            'status': 'Success kinda'
        }
        return response_object, 202


def get_all_blogs():
    return Blog.query.all()


def get_one_blog(title):
    return Blog.query.filter_by(title=title).first()


def save_blog(data):
    db.session.add(data)
    db.session.commit()
