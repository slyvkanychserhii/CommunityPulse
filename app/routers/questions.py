from flask import Blueprint, request, jsonify
from app.models import Question, Category
from app.schemas.question import QuestionCreate, QuestionResponse
from app.models import db
from pydantic import ValidationError


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    questions = Question.query.all()
    # Сериализуем объекты SQLAlchemy в Pydantic модели
    results = [QuestionResponse.from_orm(question).dict() for question in questions]
    return jsonify(results)


@questions_bp.route('/', methods=['POST'])
def create_question():
    """Создание нового вопроса."""
    data = request.get_json()
    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.errors()), 400
    category = Category.query.get(question_data.category_id)
    if not category:
        return jsonify({"message": "Категория с таким ID не найдена"}), 404
    question = Question(text=question_data.text, category_id=category.id)
    db.session.add(question)
    db.session.commit()
    return jsonify(QuestionResponse.from_orm(question).dict()), 201


@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Получение деталей конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404
    return jsonify(QuestionResponse.from_orm(question).dict()), 200


@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404
    data = request.get_json()
    if 'text' in data:
        question.text = data['text']
    if 'category_id' in data:
        question.category_id = data['category_id']
    db.session.commit()
    return jsonify(QuestionResponse.from_orm(question).dict()), 200


@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': f"Вопрос с ID {id} удален"}), 200
