
## Prerequisites

Before running the bot, ensure you have the following:

- Python 3.7 or higher installed.
- A Telegram account.
- A Telegram bot token (see below for instructions).
- A `.env` file to store your environment variables (Refer .env.example)
---

## Getting Started

### How to Get a Telegram Bot Token

1. Open Telegram and search for the **BotFather** (Telegram's official bot for creating and managing bots).
2. Start a chat with BotFather and use the `/newbot` command.
3. Follow the instructions:
   - Choose a name for your bot (e.g., `MyTestBot`).
   - Choose a username for your bot (must end with `bot`, e.g., `MyTestBot_bot`).
4. Once the bot is created, BotFather will provide you with a **token**. This token is your `TELEGRAM_BOT_TOKEN`.
   Example token: 123456789:ABCdefGhIJKlmNoPQRstuVWXyz
5. Save this token for later use.

---

Okay - that's it. I used this most of the time to send alerts for my memecoins, and trading strategy. Alternatively, we can use Telebot and polling approach to receive real time message with commands.
