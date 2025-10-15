# 📚 StudyBuddy – A Discord Bot for Students

StudyBuddy is a Discord bot built with Python that helps students stay focused and organized. It includes built-in **Pomodoro timers**, **flashcard quizzes**, and **productivity tools** right inside your Discord server.

---

## ✨ Features

* 🍅 `!pomodoro start` – Start a 25-minute focus timer (default)
* ⏱️ `!pomodoro long` – Start an extended 50-minute focus timer with a 10-minute break
* ☕ `!pomodoro break` – Begin a manual break (in process)
* 📖 `!card add "Question" | "Answer"` – Add a custom flashcard 
* 🧠 `!quiz` – Test yourself with random flashcards
* 🎯 `!stats` – Track quiz performance *(coming soon)*
* 🔔 Optional group mode & DMs for reminders

Timers use asynchronous scheduling so multiple users can study independently without blocking each other.

---

## ⚙️ Setup Instructions

1. **Clone the Repo**

   ```bash
   git clone https://github.com/yourusername/studybuddy-bot.git
   cd studybuddy-bot
   ```

2. **Install Dependencies**
   Requires **Python 3.10+**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**

   ```bash
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

4. **Run the Bot**

   ```bash
   python main.py
   ```

---

## 🧠 Flashcard Commands

| Command                        | Description                |                     |
| ------------------------------ | -------------------------- | ------------------- |
| `!card add "Question"          | "Answer"`                  | Add a new flashcard |
| `!quiz`                        | Start flashcard quiz mode  |                     |
| *(Future)* `!card list`        | View your saved flashcards |                     |
| *(Future)* `!card delete <id>` | Remove a flashcard by ID   |                     |

Flashcards are stored per user using a local **SQLite database**, ensuring persistence between restarts.

---

## ⏱️ Pomodoro Commands

| Command            | Description                        |
| ------------------ | ---------------------------------- |
| `!pomodoro start`  | Start a 25-minute Pomodoro session |
| `!pomodoro long`   | Start a 50-minute extended session |
| `!pomodoro status` | Check how much time remains        |
| `!pomodoro cancel` | Cancel your active timer           |

Pomodoros automatically include a 5-minute or 10-minute break when finished.
Each user’s session runs independently using Python’s `asyncio`.

---

## 🔐 Bot Permissions

Make sure your bot has these **permissions** in your Discord server:

* Send Messages
* Read Message History
* Embed Links
* Use Slash Commands *(optional)*
* Add Reactions *(for interactive features)*

And enable the following **Privileged Gateway Intents** in the [Discord Developer Portal](https://discord.com/developers/applications):

* Message Content Intent
* Server Members Intent

---

## 📦 Project Structure

```
studybuddy-bot/
│
├── main.py               # Main bot logic and command routing
├── pomodoro.py           # Pomodoro timers (standard + long sessions)
├── flashcards.py         # Flashcard management and SQLite integration
├── .env                  # Discord bot token (excluded from Git)
├── .gitignore            # Ignored files and directories
└── requirements.txt      # Dependencies
```

---

## 🚀 Roadmap

* [ ] Add custom Pomodoro durations (`!pomodoro custom <minutes>`)
* [ ] Add daily flashcard reminders via DM
* [ ] Implement stats tracking for Pomodoro and quizzes
* [ ] Support slash commands for Discord UI integration
* [ ] Web dashboard to view flashcards and session data

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
