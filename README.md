# 🐣 ProjectHatch

> Your AI that learns what you need, builds what you don't have.

**Made for the people. By Paul Sudo.**

## What Is This?

ProjectHatch makes ANY language model feel premium through smart routing between free local models and paid cloud APIs. It learns, builds tools, and respects your budget.

### Key Features

- 🧠 **Smart Routing** - Automatically picks the best model for each task
- 💰 **Budget Protection** - Never exceeds your spending limits
- 🔒 **Privacy First** - Runs locally by default, cloud only with permission
- 🛠️ **Tool Building** - Learns new capabilities and saves them
- 👁️ **Vision Support** - Works even with text-only models
- 🌐 **Curated Learning** - Fetches info from safe, whitelisted sites

## Quick Start

### 1. Install Ollama (if you don't have it)

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Download a model

```bash
ollama pull qwen2.5:3b
```

### 3. Install ProjectHatch

```bash
git clone https://github.com/yourusername/projecthatch
cd projecthatch
pip install -r requirements.txt
```

### 4. Run!

```bash
python main.py
```

## How It Works

```
You: "build me a web scraper"
  ↓
Hatch analyzes complexity
  ↓
Offers choice: local (free) or cloud ($0.15)
  ↓
You choose
  ↓
Hatch builds it, saves as reusable tool
  ↓
Next time: instant
```

## Budget Control

Set daily spending limits:

```python
# In config: ~/.projecthatch/config.json
{
  "budget": {
    "daily_limit": 5.00  // $5/day default
  }
}
```

Hatch will:
- ✅ Warn at 75%, 90% usage
- ✅ Ask permission before expensive queries
- ✅ Never exceed limit without override

## Commands

In chat:
- `help` - Show commands
- `budget` - Check spending
- `@local <query>` - Force local model
- `@cloud <query>` - Force cloud model
- `quit` - Exit

## Cloud APIs (Optional)

Add API keys for better quality on complex tasks:

```bash
# Edit: ~/.projecthatch/config.json
{
  "cloud_apis": {
    "openai": {
      "enabled": true,
      "key": "sk-..."
    },
    "anthropic": {
      "enabled": true,
      "key": "sk-ant-..."
    },
    "google": {
      "enabled": true,
      "key": "..."
    }
  }
}
```

## System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- 10GB disk space

**Recommended:**
- Python 3.10+
- 8GB RAM
- 20GB disk space

**Runs on:**
- Ubuntu/Debian
- macOS
- Windows (via WSL)
- Raspberry Pi 4/5

## Philosophy

> "AI for the people. Not for exploitation."

ProjectHatch exists so that someone with:
- A $200 laptop
- Limited internet
- No money for subscriptions

...can still have an AI buddy that works hard for them.

## Disclaimer

⚖️ This is experimental software provided "as-is" under the AGPLv3 License.

- No warranty or guarantees
- May incur API costs (you control budget)
- May modify files (with permission)
- Use at your own risk

See LICENSE for full details.

## Roadmap

- ✅ v0.1: CLI + smart routing + budget (current)
- 🚧 v0.2: Web UI + Telegram bot + eSIM integration
- 🔮 v0.3: Self-improvement loop
- 🔮 v0.4: Model distillation

## Contributing

Issues and PRs welcome! See CONTRIBUTING.md

## License

MIT License - see LICENSE file

Copyright (c) 2024 Paul Sudo

---

Built with ❤️ for the builders who can't afford $200/month in AI costs.
