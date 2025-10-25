# WBNotifier - Personal Telegram bot assistant for Wildberries sellers.
**In short:**  
🟪 **WBNotifier** is a lightweight and reliable Telegram bot that automatically monitors your Wildberries product data and notifies you about important changes.  
It also lets you quickly access essential information — such as orders, prices, and stock levels — in one click.  
The project started as a practical tool for a single seller and is designed for future scalability and potential commercial use.

![logo](assets/logo.gif)

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
## 🎬 Demo
Here’s how WBNotifier works in action:
<p float="left">
  <img src="assets/1.gif" width="300" />
  <img src="assets/2.gif" width="300" />
  <img src="assets/3.gif" width="300" />
</p>


---
## 🧠 Tech Stack

- 🐍 Python 3.13+
- 🤖 aiogram 3.22
- 🌐 requests
    - _Although aiogram is fully asynchronous, the current version of WBNotifier uses the requests library for simplicity and stability.
Since the project currently serves a single user, the performance difference is negligible, and asynchronous HTTP calls were not required at this stage.
This approach keeps the codebase simpler while maintaining reliability._
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
## 🗓️ Plans for the Near Future

- **Support for multiple users and multiple products** (currently only one product can be monitored).  
- **Commercial SaaS version** with subscription-based access.  
- **Migration to asynchronous HTTP requests using aiohttp** for improved scalability and performance once multi-user support is introduced.  
- **Automated stock and price management** — future releases will include features like adjusting stock quantities and managing prices (including automated, data-driven dynamic pricing) directly within the bot.  
- **Dedicated PostgreSQL database** to store historical data such as price changes, sales analytics, and monthly summaries (e.g., gross profit, number of units sold, etc.).  
- **Transformation from an informative assistant to a smart management tool** — WBNotifier will evolve into a true helper that not only informs but also acts.  
- 💬 **Open to feedback and ideas** — if you have any suggestions for improvement, I’d be glad to hear them!

---
## Feedback & Collaboration 🤝

- WBNotifier is still growing — and I’m always open to feedback, insights, and professional advice.  
- If you’re an experienced developer, your technical recommendations are very welcome.  
- If you’re a fellow Wildberries seller, I’d love to hear what features or problems matter most to you — your input directly shapes the direction of the project.
- In the future, as WBNotifier evolves into a commercial tool, sellers will become its core users — and your early ideas can help build something truly useful.
- You can share your thoughts or suggestions by opening an issue or contacting me directly.

---
## 📜 License

Distributed under the Custom Proprietary License. See [LICENSE](LICENSE) for more information.
