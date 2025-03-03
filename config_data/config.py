import os
from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

load_dotenv()

class SiteSettings(BaseSettings):
    """
    Настройки для приложения.
    """
    # api_key: SecretStr = os.getenv('SITE_API', None)
    # host_api: StrictStr = os.getenv('HOST_API', None)
    bot_token: SecretStr = os.getenv('BOT_TOKEN', None)

    class Config:
        env_file = '.env'  # Указание файла с переменными окружения

DEFAULT_COMMANDS = (
    ('start', 'Начало работы'),
    ('search_by_name', 'Поиск фильма по названию'),
    ('search_by_year_and_country', 'Поиск фильмов по стране и году'),
    ('search_by_rating', 'Поиск фильмов по рейтингу'),
    ('random_movie', 'Рандомный поиск фильмов'),
    ('history', 'История запросов поиска фильмов'),
    ('help', 'Помощь'),
)

DATABASE_URL = "sqlite:///./my_bot.db"
