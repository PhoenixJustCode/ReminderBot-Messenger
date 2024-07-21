import asyncio
from telethon import TelegramClient, events


class TelegramBot:
    def __init__(self, api_id, api_hash, bot_username, session_name='session_name.session'):
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_username = bot_username
        self.session_name = session_name
        self.client = TelegramClient(
            self.session_name, self.api_id, self.api_hash)
        self.response_event = asyncio.Event()
        self.latest_message = None

    async def start(self):
        await self.client.start()
        self.client.add_event_handler(
            self.handler, events.NewMessage(chats=self.bot_username))
        print("Клиент Telegram запущен и обработчик сообщений добавлен.")

    async def send_message(self, message):
        try:
            await self.client.send_message(self.bot_username, message)
            print('Сообщение отправлено успешно')
            await self.wait_for_response()  # Wait for the response after sending the message
        except Exception as e:
            print(f'Ошибка при отправке сообщения: {e}')

    async def handler(self, event):
        print(f'Сообщение от бота: {event.message.message}')
        self.latest_message = event.message.message
        self.response_event.set()  # Signal that a response has been received

    async def wait_for_response(self):
        await self.response_event.wait()  # Wait for the response event to be set
        print(f'Ответ бота: {self.latest_message}')
        self.response_event.clear()  # Clear the event for the next message

    async def run_until_disconnected(self):
        await self.client.run_until_disconnected()
