from flask import request
from flask_restx import Resource

from ..util.dto import BlogDto
from ..service.blog_service import save_new_blog, get_all_blogs, get_one_blog

api = BlogDto.api
_blog = BlogDto.blog


@api.route('/')
class Bloglist(Resource):
    @api.doc('list_of_blogs')
    @api.marshal_list_with(_blog, envelope='data')
    def get(self):
        """list all blogs"""
        return get_all_blogs()

    @api.response(201, "blog updated/added")
    @api.doc('create or update a blog')
    @api.expect(_blog, validate=True)
    def post(self):
        """ Creates/ updates Blog"""
        data = request.json
        return save_new_blog(data)


@api.route('/<title>')
@api.param('id', 'The blog identifier')
@api.response(404, "Blog not found.")
class Blog(Resource):
    @api.doc('get a blog')
    @api.marshal_list_with(_blog)
    def get(self, title):
        """get blog with given title"""
        blog = get_one_blog(title)
        if not blog:
            api.abort(404)
        else:
            return blog
