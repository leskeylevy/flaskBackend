import flask
from flask_restx import Resource

from ..util.dto import BlogDto
from ..service.blog_service import save_new_blog, get_all_blogs, get_one_blog, edit_blog, get_all_published_blogs

api = BlogDto.api
_blog = BlogDto.blog


@api.route('/')
class Bloglist(Resource):
    @api.doc('list_of_blogs')
    @api.marshal_list_with(_blog, envelope='data')
    def get(self):
        """list all blogs"""
        return get_all_blogs()


@api.route('/published')
class PublishedBloglist(Resource):
    @api.doc('list_of_published_blogs')
    @api.marshal_list_with(_blog, envelope='data')
    def get(self):
        """list all published blogs"""
        return get_all_published_blogs()


@api.route('/editBlog')
@api.response(200, "blog updated/added")
class AddBlog(Resource):
    @api.doc('create or update a blog')
    @api.expect(_blog, validate=True)
    def post(self):
        """updates Blog"""
        data = flask.request.json
        return edit_blog(data)


@api.route('/addBlog')
@api.response(200, "blog added")
class AddBlog(Resource):
    @api.doc('create or update a blog')
    @api.expect(_blog, validate=True)
    def post(self):
        """creates Blog"""
        data = flask.request.json
        return save_new_blog(data)


@api.route('/one')
@api.param('slug', 'The blog identifier')
@api.response(404, "Blog not found.")
class Blog(Resource):
    @api.doc('get one blog')
    @api.marshal_list_with(_blog)
    def post(self):
        """get blog with given title"""
        slug = flask.request.json['slug']
        blog = get_one_blog(slug)
        if not blog:
            return 404
        else:
            return blog
