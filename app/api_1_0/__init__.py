from flask import Blueprint
from flask import jsonify, abort
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

@api.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    response = jsonify({'question': question[0]}) 
    response.status_code = 200
    return response    