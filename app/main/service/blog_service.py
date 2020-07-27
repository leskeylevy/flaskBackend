import datetime
import slugify

from app.main import db
from app.main.model.blog import Blog


def save_new_blog(data):
    new_blog = Blog(
        title=data['title'],
        content=data['content'],
        created_on=datetime.datetime.utcnow(),
        status=data['status'],
        caption=data['caption'],
        img=data['img'],
        author_id=data['author_id'],
        slug=data['slug'],
        updated_on=datetime.datetime.utcnow()
    )
    save_blog(new_blog)
    response_object = {
        "status": 'Success',
        "message": 'Successfuly added blog'
    }
    return response_object, 201


def edit_blog(data):
    blog = Blog.query.filter_by(id=data['id']).first()
    if blog:
        blog.title = data['title']
        blog.content = data['content']
        blog.status = data['status']
        blog.caption = data['caption']
        blog.update_on = datetime.datetime.utcnow()
        blog.author_id = data['author_id']
        blog.img = data['img']
        blog.slug = data['slug']
        db.session.commit()

        response_object = {
            'message': "Successfuly edited blog",
            'status': 'Success kinda'
        }
        return response_object, 202
    else:
        response_object = {
            'message': 'Failed Blog not edited!',
            'status': 'Failed!'
        }
        return response_object, 235


def get_all_blogs():
    return Blog.query.order_by(Blog.created_on.desc()).all()


def get_all_published_blogs():
    return Blog.query.filter_by(status='1').order_by(Blog.created_on.desc()).all()


def get_one_blog(slug):
    post = Blog.query.filter_by(slug=slug).first()
    return post


def save_blog(data):
    db.session.add(data)
    db.session.commit()
