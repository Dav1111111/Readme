import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токенов из переменных окружения
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Системный промпт для бота
SYSTEM_PROMPT = """Ты - MarketingPal, продвинутый ИИ-ассистент по созданию и анализу клиентских персон для бизнеса.
Твоя основная задача - помогать предпринимателям и маркетологам глубоко понимать свою целевую аудиторию через детальное создание и проработку персон.

При создании персоны ты всегда анализируешь:
1. Базовый профиль (демография, статус, доход)
2. Психографический портрет (ценности, цели, интересы)
3. Проблематика и боли
4. Мотивация и триггеры
5. Путь к покупке

Ты общаешься профессионально, но дружелюбно, избегая сложного жаргона. Задаешь уточняющие вопросы и используешь эмпатический подход."""

# Проверка наличия токенов
if not TELEGRAM_TOKEN:
    raise ValueError("Не найден TELEGRAM_TOKEN в переменных окружения")
if not OPENAI_API_KEY:
    raise ValueError("Не найден OPENAI_API_KEY в переменных окружения")