# main.py
# from telebot.custom_filters import StateFilter
from loader import bot
# from database.db import create_tables
import handlers

# Настройка логирования
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Точка входа в приложение.

    Создает таблицы в базе данных, добавляет кастомные фильтры для бота и запускает бота.
    """
    # Создаем таблицы в базе данных
    # create_tables()
    logger.info("Таблицы созданы успешно.")

    # Добавляем кастомные фильтры для бота
    # bot.add_custom_filter(StateFilter(bot))

    # Запускаем бота
    logger.info("Bot started polling...")
    bot.polling()


if __name__ == "__main__":
    main()
