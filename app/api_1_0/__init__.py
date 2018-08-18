from flask import Blueprint
from flask import jsonify
api = Blueprint('api', __name__)


questions = [
    {
        'id': 1,
        'question': 'What is the ...'},
    {
        'id': 2,
        'question': 'How would ...'}
]

@api.route('/questions/', methods=['GET'])
def get_questions():
    response = jsonify({'questions': questions})
    response.status_code = 200
    return response
     