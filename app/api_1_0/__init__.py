from flask import Blueprint
from flask import jsonify, abort, request
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

@api.route('/questions/', methods=['POST'])
def create_question():
    if not request.json or not 'question' in request.json:
        abort(400)
    question = {
        'id': questions[-1]['id'] + 1,
        'questiion': request.json['question'],
        }
    questions.append(question)
    response = jsonify({'questiion': question})
    response.status_code = 201
    return response