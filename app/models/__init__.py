from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

from app.models.categories import *
from app.models.questions import *
from app.models.responses import *


# flask db init - # Инициализирует миграции (Создает папки "migrations" и "instance")
# flask db migrate -m "Initial migration" - # Создает файлы миграции (Создает базу данных (с одной
#       таблицей "alembic_version") в папке "instance" и миграцию "migrations/versions/2c11e1c710ca_.py")
# flask db upgrade # Применяет миграции к базе данных (Создает в базе данных таблицы моделей)
# flask db downgrade # Откатывает последнюю миграцию
# flask db history
# flask db downgrade 800de9b841e7 # Откатывает миграцию 800de9b841e7


# cd instance
# sqlite3
#
# .mode column  # включить красивый вывод табличных данных
# .open foo.db  # подключиться к БД ()
# .tables  # просмотреть таблицы БД
# PRAGMA table_info(categories);  # показать информацию о таблице "categories"
# PRAGMA table_info(questions);  # показать информацию о таблице "questions"
# PRAGMA foreign_key_list(questions);  # показать информацию о таблице "questions"
# PRAGMA foreign_key_list(responses);  # показать информацию о таблице "responses"
# SELECT sql FROM sqlite_master WHERE type='table' AND name='responses';  # показать скрипт SQL которым
#                                                                           была создана таблица "responses"
#
# DELETE FROM questions; DELETE FROM statistics; DELETE FROM responses; DELETE FROM categories;
# SELECT * FROM questions;
