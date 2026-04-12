#!/usr/bin/env python3
"""ProjectHatch - AI cognitive amplification for everyone."""
import json
import sys
from pathlib import Path

# Default config
DEFAULT_CONFIG = {
    "disclaimer_accepted": False,
    "mode": "normie",
    "budget": {
        "daily_limit": 5.00
    },
    "cloud_apis": {
        "openai": {"enabled": False, "key": ""},
        "anthropic": {"enabled": False, "key": ""},
        "google": {"enabled": False, "key": ""}
    },
    "permissions": {
        "file_write": "ask_first",
        "web_search": "ask_first",
        "code_exec": "ask_first"
    }
}

def load_config():
    """Load or create config."""
    config_dir = Path.home() / ".projecthatch"
    config_file = config_dir / "config.json"
    
    if config_file.exists():
        with open(config_file) as f:
            return json.load(f)
    else:
        config_dir.mkdir(exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
        return DEFAULT_CONFIG

def main():
    """Main entry point."""
    print("""
╦ ╦╔═╗╔╦╗╔═╗╦ ╦
╠═╣╠═╣ ║ ║  ╠═╣
╩ ╩╩ ╩ ╩ ╚═╝╩ ╩
ProjectHatch v0.1 - Made for the people
""")
    
    config = load_config()
    
    # Run CLI mode
    from ui.cli import main as cli_main
    cli_main(config)

if __name__ == "__main__":
    main()
