import asyncio

from SpeechRecognizer import SpeechRecognizer
from TelegramBot import TelegramBot
from ConsoleOutput import ConsoleOutput

API_ID = '29776585'
API_HASH = '0e85ed227dfa5ac9a2ac232659338076'
BOT_USERNAME = 'hidola1bot'


class MainApplication:
    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        self.telegram_bot = TelegramBot(API_ID, API_HASH, BOT_USERNAME)
        self.console_output = ConsoleOutput()

    async def process_speech(self):
        while True:
            text = self.speech_recognizer.recognize_speech()
            if text and "хей" in text.lower():
                message = text.lower().replace('хей', '').strip()
                await self.telegram_bot.send_message(message)
                # Wait for the response before continuing
                await self.telegram_bot.wait_for_response()

    async def run(self):
        await self.telegram_bot.start()  # Start the Telegram client
        await self.process_speech()


if __name__ == '__main__':
    app = MainApplication()
    asyncio.run(app.run())
