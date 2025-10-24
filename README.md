# WBNotifier - Personal Telegram bot assistant for Wildberries sellers.
**In short:**  
🟪 **WBNotifier** is a lightweight and reliable Telegram bot that automatically monitors your Wildberries product data and notifies you about important changes.  
It also lets you quickly access essential information — such as orders, prices, and stock levels — in one click.  
The project started as a practical tool for a single seller and is designed for future scalability and potential commercial use.

---
## 💡 Why It Matters (Business Problem)

Marketplace sellers (like me) face several operational challenges:
- 🔻 **Unnotified price changes:** Wildberries often applies automatic discounts without alerting the seller, which can affect profit margins.
- 📉 **Stock issues:** Products can sell out unnoticed, and new orders may be missed unless the dashboard is constantly checked.
- 🔄 **Manual price comparison:** Comparing your price with the main supplier’s (in both countries) requires too many steps and manual effort.

**WBNotifier** solves these problems by pulling data from the **Wildberries Seller API** and **supplier API**, checking for updates on schedule, and sending instant Telegram alerts — saving time, preventing losses, and providing full visibility over your pricing and stock.

---
## ⚙️ Key Features

#### 🔁 Automated Monitoring (every 15 minutes)
- **New Orders:** Displays order country, price, date, and time.
- **Price Changes:** Shows the previous and new price.
- **Price Comparison:** Compares your price with the supplier’s (in both your and their country).
- **Stock Check:** Alerts when stock reaches zero.
#### 🤖 Bot Commands / Buttons
- **▶️ /start** — Welcome message and interactive buttons.
- **🆕 Orders (FBS)** — Lists recent orders (with quantity, country, price, and date/time).
- **💵 Price of My Goods** — Displays 4 prices: yours and supplier’s in both countries.
- **📦 Number of Goods in Stock** — Shows current stock level.
---
## 🧠 Tech Stack

- 🐍 Python 3.13+
- 🤖 aiogram 3.22
- 🌐 requests
---
## 🧩 Architecture

- **`main.py`** — main bot script
    - `scheduled_task` (asyncio/cron) — performs periodic API checks and compares data with saved states.
    - Message-sending logic.
- **orders/price/stock managers (`*_managers_class.py`)** — class-based managers for saving, updating, comparing, and returning data from APIs. Core logic for fetching and processing information.
- **`utilities.py`**
    - `get_exchange_rate()` — returns current exchange rate for given currencies.
    - `format_datetime()` — returns formatted date/time string.
    - `get_country_name_by_code()` — returns full country name by currency code.
- **`config.py`** _(excluded from repo)_ — contains configuration data: tokens, endpoints, product IDs, etc.
---
## 🚀 Plans for the Near Future

- Support for **multiple users** and **multiple products** (currently only one product can be monitored).
- Commercial **SaaS version** with subscription-based access.

In the long run, this is just the beginning.  
Future releases will introduce features like **stock adjustment** and **price management** (including automated, data-driven dynamic pricing) directly within the bot.
While **WBNotifier** currently serves mainly as an **informative assistant**, it will evolve into a **smart management tool** — a true helper that not only informs but also acts.
A dedicated **PostgreSQL database** is also planned to store historical data — including price changes, sales analytics, and monthly summaries (e.g., gross profit, number of units sold, etc.).
💬 _If you have any ideas or suggestions for improvement, I’d be glad to hear them!_

---
## Feedback & Collaboration 🤝

WBNotifier is still growing — and I’m always open to feedback, insights, and professional advice.  
If you’re an experienced developer, your technical recommendations are very welcome.  
If you’re a fellow Wildberries seller, I’d love to hear what features or problems matter most to you — your input directly shapes the direction of the project.

In the future, as WBNotifier evolves into a commercial tool, sellers will become its core users — and your early ideas can help build something truly useful.

You can share your thoughts or suggestions by opening an issue or contacting me directly.

---
## 📜 License

Distributed under the Custom Proprietary License. See LICENSE for more information.
