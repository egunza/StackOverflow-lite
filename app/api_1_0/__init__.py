from flask import Blueprint
from flask import jsonify, abort, request
api = Blueprint('api', __name__)


questions = [
    {
        'id': 1,
        'question': 'What is the ...'},
    {
        'id': 2,
        'question': 'How would ...'},
    {
        'id': 3,
        'question': 'Is TDD a preferred method in ...'}
]

answers = [{
        'id': 1,
        'answer': 'All editors are ...',
        'question_id':2
        },
        {
        'id': 2,
        'answer': 'The most important ...',
        'question_id':1
        },
        {
        'id': 3,
        'answer': 'What is th second ...',
        'question_id':1
        }]


@api.route('/questions/<int:question_id>/answers/', methods=['POST'], strict_slashes=False)
def create_answer(question_id):
    if not request.json or not 'answer' in request.json:
        abort(400)
    answer = {
        'id': answers[-1]['id'] + 1,
        'answer': request.json['answer'],
        'question_id':question_id
        }
    answers.append(answer)
    response = jsonify({'answer': answer})
    response.status_code = 201
    return response

@api.route('/questions/', methods=['GET'], strict_slashes=False)
def get_questions():
    response = jsonify({'questions': questions})
    response.status_code = 200
    return response

@api.route('/questions/<int:question_id>/', methods=['GET'], strict_slashes=False)
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    response = jsonify({'question': question[0]}) 
    response.status_code = 200
    return response    

@api.route('/questions/', methods=['POST'], strict_slashes=False)
def create_question():
    if not request.json or not 'question' in request.json:
        abort(400)
    question = {
        'id': questions[-1]['id'] + 1,
        'questiion': request.json['question'],
        }
    questions.append(question)
    response = jsonify({'question': question})
    response.status_code = 201
    return response

@api.route('/questions/<int:question_id>/', methods=['DELETE'], strict_slashes=False)
def delete_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({'result': True})



@api.route('/questions/<int:question_id>/answers/', methods=['GET'], strict_slashes=False)
def get_answers(question_id):
    ans = [answer for answer in answers if answer['question_id'] == question_id]
    response = jsonify({'answers': ans}) 
    response.status_code = 200
    return response
