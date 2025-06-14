import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# List of URLs to capture with individual settings
URLS = [
    {
        "name": "option_chain",
        "url": "https://web.sensibull.com/option-chain?view=ltp",
        "scale": 0.6,
        "page_ranges": ["1"],
        "landscape": False  # True for landscape, False for portrait
    },
    {
        "name": "option_chain_greeks",
        "url": "https://web.sensibull.com/option-chain?view=greeks",
        "scale": 0.6,
        "page_ranges": ["1"],
        "landscape": False
    },
    {
        "name": "oi_change_vs_strike",
        "url": "https://web.sensibull.com/open-interest/oi-change-vs-strike?tradingsymbol=NIFTY",
        "scale": 0.7,
        "page_ranges": ["1"],
        "landscape": True
    },
    {
        "name": "multistrike_oi",
        "url": "https://web.sensibull.com/open-interest/multistrike-oi?tradingsymbol=NIFTY",
        "scale": 0.7,
        "page_ranges": ["2"],
        "landscape": True
    },
    {
        "name": "oi_vs_time",
        "url": "https://web.sensibull.com/open-interest/oi-vs-time?tradingsymbol=NIFTY",
        "scale": 0.8,
        "page_ranges": ["1"],
        "landscape": True  # Portrait for charts
    },
    {
        "name": "fut_oi_vs_time",
        "url": "https://web.sensibull.com/open-interest/fut-oi-vs-time?tradingsymbol=NIFTY",
        "scale": 0.8,
        "page_ranges": ["1"],
        "landscape": True  # Portrait for charts
    },
    {
        "name": "fii_dii_data",
        "url": "https://web.sensibull.com/fii-dii-data",
        "scale": 0.8,
        "page_ranges": ["1"],
        "landscape": False,
        "pre_print_actions": [
            {
                "action": "click",
                "selector": "//button[.//p[contains(text(), 'Index Futures')]]",  # Click Index Futures dropdown by text using XPath
                "selector_type": "xpath", 
                "wait_after": 2
            },
            {
                "action": "click_all",
                "selector": "//button[.//p[contains(text(), 'Index Options')]]",  # Click ALL Index Options buttons
                "selector_type": "xpath", 
                "wait_after": 2     # Wait 2 seconds after all clicks are done
            }
        ]
    },
    {
        "name": "fii_dii_fno-fii",
        "url": "https://web.sensibull.com/fii-dii-data/fno",
        "scale": 0.8,
        "page_ranges": ["1-4"],
        "landscape": True,
        "pre_print_actions": [
            {
                "action": "click",
                "selector": "button#radix-16-trigger-fii",  # Click the Pro tab button
                "selector_type": "css", 
                "wait_after": 2
            }
        ]
    },
    {
        "name": "fii_dii_fno-pro",
        "url": "https://web.sensibull.com/fii-dii-data/fno",
        "scale": 0.8,
        "page_ranges": ["1-4"],
        "landscape": True,
        "pre_print_actions": [
            {
                "action": "click",
                "selector": "button#radix-16-trigger-pro",  # Click the Pro tab button
                "selector_type": "css", 
                "wait_after": 2
            }
        ]
    },
        {
        "name": "fii_dii_fno-client",
        "url": "https://web.sensibull.com/fii-dii-data/fno",
        "scale": 0.8,
        "page_ranges": ["1-4"],
        "landscape": True,
        "pre_print_actions": [
            {
                "action": "click",
                "selector": "button#radix-16-trigger-client",  # Click the Client tab button
                "selector_type": "css", 
                "wait_after": 2
            }
        ]
    },
    {
        "name": "fii_dii_cash_market",
        "url": "https://web.sensibull.com/fii-dii-data/cash-market",
        "scale": 0.8,
        "page_ranges": ["1-2"],
        "landscape": True
    },
    {
        "name": "fii_dii_history",
        "url": "https://web.sensibull.com/fii-dii-data/history",
        "scale": 0.8,
        "page_ranges": ["1-2"],
        "landscape": True
    },
    {
        "name": "futures_options_data",
        "url": "https://web.sensibull.com/futures-options-data?tradingsymbol=NIFTY",
        "scale": 0.8,
        "page_ranges": ["1"],
        "landscape": False
    },
    {
        "name": "daily_nifty_analysis",
        "url": f"https://web.sensibull.com/daily-nifty-analysis?lang=english&date={datetime.now().strftime('%Y-%m-%d')}",
        "scale": 0.8,
        "page_ranges": ["1-4"],
        "landscape": False  # Portrait for analysis
    }
]

# Additional configuration settings
PDF_SETTINGS = {
    "default_scale": 0.5,
    "default_page_ranges": ["1"],
    "landscape": True,
    "format": "A4",
    "margins": {
        "top": 0.2,
        "bottom": 0.2,
        "left": 0.2,
        "right": 0.2
    },
    # "displayHeaderFooter": False

}

# Browser settings
BROWSER_SETTINGS = {
    "window_size": (1920, 1080),
    "headless": True,
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
}

# Telegram settings
TELEGRAM_SETTINGS = {
    "enabled": True,  # Set to True to enable Telegram
    "bot_token": os.getenv("TELEGRAM_BOT_TOKEN", ""),  # Read from .env file
    "chat_id": os.getenv("TELEGRAM_CHAT_ID", ""),  # Read from .env file
    "message": "📊 Daily Sensibull Report for {date} is ready!"
}

# Note: Bot token and chat ID are now stored securely in .env file
# This prevents accidental commits of sensitive information to version control
