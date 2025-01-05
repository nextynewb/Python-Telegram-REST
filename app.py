import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TelegramBot:
    BASE_URL = "https://api.telegram.org/bot"

    def __init__(self, token=None):
        try:
            self.token = token or os.getenv('TELEGRAM_BOT_TOKEN')
            if not self.token:
                raise ValueError("Telegram Bot Token is required")
            self.url = self.BASE_URL + self.token
        except Exception as e:
            raise Exception(f"Error initializing bot: {str(e)}")

    def send_message(self, chat_id, text):
        try:
            url = self.url + "/sendMessage"
            data = {"chat_id": chat_id, "text": text}
            response = requests.post(url, data=data)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error while sending message: {str(e)}")
            return None

    def check_updates(self):
        try:
            url = self.url + "/getUpdates"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error checking updates: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error while checking updates: {str(e)}")
            return None

    def get_chat_id(self, username):
        try:
            url = self.url + "/getUpdates"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("ok"):
                raise ValueError("Failed to get updates from Telegram")
                
            for result in data.get("result", []):
                sender = result.get('message', {}).get('from', {})
                if sender.get('username') == username:
                    return result['message']['chat']['id']
            
            return "Username not found in recent updates"
            
        except requests.exceptions.RequestException as e:
            print(f"Error getting chat ID: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error while getting chat ID: {str(e)}")
            return None



"""
Example usage:

    1. Create a new bot on Telegram to get key @BotFather
    2. Get your chat ID by sending a message to your bot and checking the updates (you can run bot.get_chat_id('YOUR_USERNAME'))
    3. Replace YOUR_CHAT_ID and YOUR_MESSAGE with your chat ID and message respectively
"""
bot = TelegramBot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
bot.send_message('YOUR_CHAT_ID', 'YOUR_MESSAGE')
bot.get_chat_id('YOUR_USERNAME') # @yadda_yadda = yadda_yadda etc
