from flask import request
from flask_restx import Resource

from ..util.dto import CommentsDto
from ..service.comment_service import save_new_comment, get_all_comments

api = CommentsDto.api
_comment = CommentsDto.comment


@api.route('/add')
class Comment(Resource):
    @api.doc('create a new comment')
    @api.expect(_comment, validate=True)
    def post(self):
        """Creates a comment """
        data = request.json
        return save_new_comment(data=data)
        # return data


@api.route('/<blog_id>')
@api.param('blog_id', 'The blog Identifier')
@api.response(404, 'Blog not found,')
class CommentList(Resource):
    @api.doc('Get blog comments')
    @api.marshal_list_with(_comment, envelope='data')
    def get(self, blog_id):
        """get all comments given blog identifier"""
        comments = get_all_comments(blog_id)
        if not comments:
            # api.abort(404)
            return "Blog not found!"
        else:
            return comments
