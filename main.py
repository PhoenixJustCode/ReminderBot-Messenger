import asyncio
import speech_recognition as sr
from telethon import TelegramClient

API_ID = '29776585'
API_HASH = '0e85ed227dfa5ac9a2ac232659338076'
BOT_USERNAME = 'hidola1bot'


async def send_message_to_telegram(message):
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        try:
            await client.send_message(BOT_USERNAME, message)
            print('Сообщение отправлено успешно')
        except Exception as e:
            print(f'Ошибка при отправке сообщения: {e}')


def recognize_speech_and_send_message():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Скажите что-нибудь...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Распознавание...")
        text = recognizer.recognize_google(audio, language='ru-RU')
        print(f"Вы сказали: {text}")

        if "дола" in text:
            message = text.replace('дола', '').strip()
            asyncio.run(send_message_to_telegram(message))
        else:
            print("Активационная фраза не найдена.")

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")


if __name__ == '__main__':
    while True:
        recognize_speech_and_send_message()
