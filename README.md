# 📚 StudyBuddy – A Discord Bot for Students

StudyBuddy is a Discord bot built with Python that helps students stay focused and organized. It includes built-in **Pomodoro timers**, **flashcard quizzes**, and **productivity tools** right inside your Discord server.

---

## ✨ Features

- ⏱️ `!pomodoro start` – Start a 25-minute focus timer  
- ☕ `!pomodoro break` – Start a 5-minute break  
- 📖 `!card add "Question" | "Answer"` – Add a custom flashcard  
- 🧠 `!quiz` – Test yourself with flashcards  
- 🎯 `!stats` – Track your quiz performance  
- 🔔 Optional group mode & DMs for reminders

---

## ⚙️ Setup Instructions

1. Clone the Repo
```bash
git clone https://github.com/yourusername/studybuddy-bot.git
cd studybuddy-bot
```

2. Install Dependencies  
Make sure you're using Python 3.10 or later.

```bash
pip install -r requirements.txt
```

3. Create a `.env` File  
In the root of the project, create a `.env` file to securely store your bot token:

```
DISCORD_TOKEN=your_discord_bot_token_here
```

4. Run the Bot  
After setting everything up, launch the bot with:

```bash
python bot.py
```

---

## 🧠 Flashcard Commands

| Command | Description |
|--------|-------------|
| `!card add "Question" | "Answer"` | Add a new flashcard |
| `!card list` | View your saved flashcards |
| `!card delete <id>` | Remove a flashcard by its ID |
| `!quiz` | Start flashcard quiz mode |
| `!quit` | Exit quiz mode at any time |

Flashcards are stored per user and saved using SQLite for persistence between restarts.

---

## ⏱️ Pomodoro Commands

| Command | Description |
|--------|-------------|
| `!pomodoro start` | Start a 25-minute Pomodoro timer |
| `!pomodoro break` | Start a 5-minute break |
| `!pomodoro status` | Show current timer state |
| `!pomodoro cancel` | Cancel an active session |
| `!pomodoro group` *(optional)* | Start a timer that notifies a group role |

Timers use non-blocking `asyncio` and can support multiple users simultaneously.

---

## 🔐 Bot Permissions

Make sure your bot has the following **permissions** in your server:
- Send Messages  
- Read Message History  
- Embed Links  
- Use Slash Commands *(optional)*  
- Add Reactions *(for interactive features)*

You also need to enable these **Privileged Gateway Intents** in the [Discord Developer Portal](https://discord.com/developers/applications):
- Message Content Intent  
- Server Members Intent

---

## 📦 Project Structure

```
studybuddy-bot/
│
├── bot.py                 # Main bot logic
├── pomodoro.py            # Pomodoro session management
├── flashcards.py          # Flashcard command and DB logic
├── database.py            # SQLite wrapper for storage
├── utils.py               # Helper functions
├── .env                   # Bot token (not committed)
└── requirements.txt       # Project dependencies
```

---

## 🚀 Roadmap

- [ ] Add daily flashcard reminders via DM  
- [ ] Flashcard import/export (JSON or CSV)  
- [ ] Slash command support  
- [ ] Group leaderboard for quiz performance  
- [ ] Web dashboard to manage flashcards  

---

## 🤝 Contributing

Pull requests are welcome!  
Please open an issue first to discuss major changes.

---

## 🪪 License

MIT License  
Copyright © 2025  
Maintained by [Chris](https://github.com/Chrisvrsa)

---

## 💬 Need Help?

Join the discussion in our [Discord server](https://discord.gg/yourserverlink) or open an issue on GitHub.
