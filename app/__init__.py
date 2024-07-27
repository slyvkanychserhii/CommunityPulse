from flask import Flask
from flask_migrate import Migrate
from app.routers.questions import questions_bp
from app.routers.response import response_bp
from config import DevelopmentConfig
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)
    return app

# flask db init - # Инициализирует миграции (Создает папки "migrations" и "instance")
# flask db migrate -m "Initial migration" - # Создает файлы миграции (Создает базу данных (с одной
#       таблицей "alembic_version") в папке "instance" и миграцию "migrations/versions/2c11e1c710ca_.py")
# flask db upgrade # Применяет миграции к базе данных (Создает в базе данных таблицы моделей)
# flask db downgrade # Откатывает последнюю миграцию
