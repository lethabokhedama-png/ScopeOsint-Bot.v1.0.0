# ScopeOSINT Bot v1.0.0

ScopeOSINT is a Discord bot powered by SerpAPI that performs OSINT (Open-Source Intelligence) searches using Google.  
It allows users to retrieve publicly available information related to usernames, email addresses, phone numbers, and archived content.

---

## ⚙️ Requirements

- Python 3.x  
- Discord Bot Token  
- SerpAPI Key  

---

## 📁 Project Structure
ScopeOSINT/
│── main.py                # Entry point for the Discord bot 
│── utils/ 
│        ├── commands.py      # Handles Discord bot commands 
│        ├── discord.py       # Webhook + Discord messaging logic │── .env                  # Environment variables (tokens, API keys) 
│── requirements.txt      # Python dependencies

---

## 🧠 How It Works

- `main.py` initializes the Discord bot, loads environment variables, and starts the bot client.  
- `utils/commands.py` contains the command logic (e.g. searching usernames, emails, etc.).  
- `utils/discord.py` handles sending formatted results to Discord (including webhook support).  
- The bot sends queries to SerpAPI, which retrieves Google search results.  
- Results are processed and returned back to the Discord channel.

---

## 🔑 Setup

1. Clone the repository:
```bash
git clone https://github.com/lethabokhedama-png/ScopeOsint-Bot.v1.0.0/tree/main
cd scopeosint
