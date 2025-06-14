from datetime import datetime

# List of URLs to capture with individual settings
URLS = [
    # {
    #     "name": "option_chain",
    #     "url": "https://web.sensibull.com/option-chain?view=ltp",
    #     "scale": 0.6,
    #     "page_ranges": ["1"],
    #     "landscape": False  # True for landscape, False for portrait
    # },
    # {
    #     "name": "option_chain_greeks",
    #     "url": "https://web.sensibull.com/option-chain?view=greeks",
    #     "scale": 0.6,
    #     "page_ranges": ["1"],
    #     "landscape": False
    # },
    # {
    #     "name": "oi_change_vs_strike",
    #     "url": "https://web.sensibull.com/open-interest/oi-change-vs-strike?tradingsymbol=NIFTY",
    #     "scale": 0.7,
    #     "page_ranges": ["1"],
    #     "landscape": True
    # },
    # {
    #     "name": "multistrike_oi",
    #     "url": "https://web.sensibull.com/open-interest/multistrike-oi?tradingsymbol=NIFTY",
    #     "scale": 0.7,
    #     "page_ranges": ["2"],
    #     "landscape": True
    # },
    # {
    #     "name": "oi_vs_time",
    #     "url": "https://web.sensibull.com/open-interest/oi-vs-time?tradingsymbol=NIFTY",
    #     "scale": 0.8,
    #     "page_ranges": ["1"],
    #     "landscape": True  # Portrait for charts
    # },
    # {
    #     "name": "fut_oi_vs_time",
    #     "url": "https://web.sensibull.com/open-interest/fut-oi-vs-time?tradingsymbol=NIFTY",
    #     "scale": 0.8,
    #     "page_ranges": ["1"],
    #     "landscape": True  # Portrait for charts
    # },
    {
        "name": "fii_dii_data",
        "url": "https://web.sensibull.com/fii-dii-data",
        "scale": 0.5,
        "page_ranges": ["1-2"],
        "landscape": True
    },
    # {
    #     "name": "fii_dii_fno",
    #     "url": "https://web.sensibull.com/fii-dii-data/fno",
    #     "scale": 0.5,
    #     "page_ranges": ["1"],
    #     "landscape": True
    # },
    # {
    #     "name": "fii_dii_cash_market",
    #     "url": "https://web.sensibull.com/fii-dii-data/cash-market",
    #     "scale": 0.5,
    #     "page_ranges": ["1"],
    #     "landscape": True
    # },
    # {
    #     "name": "fii_dii_history",
    #     "url": "https://web.sensibull.com/fii-dii-data/history",
    #     "scale": 0.4,
    #     "page_ranges": ["1-2"],
    #     "landscape": True
    # },
    # {
    #     "name": "futures_options_data",
    #     "url": "https://web.sensibull.com/futures-options-data?tradingsymbol=NIFTY",
    #     "scale": 0.5,
    #     "page_ranges": ["1"],
    #     "landscape": True
    # },
    # {
    #     "name": "daily_nifty_analysis",
    #     "url": f"https://web.sensibull.com/daily-nifty-analysis?lang=english&date={datetime.now().strftime('%Y-%m-%d')}",
    #     "scale": 0.6,
    #     "page_ranges": ["1-2"],
    #     "landscape": False  # Portrait for analysis
    # }
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
