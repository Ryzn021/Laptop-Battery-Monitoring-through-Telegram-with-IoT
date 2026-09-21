# 🔋 Battery Notifier Bot

> **Stay ahead of battery wear!** A lightweight, cross-platform Python script that monitors your laptop's battery health and delivers real-time alert notifications directly to your **Telegram** account.

---

## 🌟 Features

* ⚡ **Smart Notifications:** Receive automated Telegram alerts when battery level drops below 20% or reaches above 80%.
* 🚀 **Ultra Lightweight:** Uses minimal CPU and RAM—no heavy web servers or continuous background polling required.
* 🌐 **Access Anywhere:** Works over the internet without local network restrictions or dynamic IP hassles.
* 💰 **100% Free:** Completely free to run with zero subscription fees or cloud service costs.
* 🛡️ **Privacy Focused:** Your hardware status is sent directly to your private Telegram bot channel.

---

## 🛠️ How It Works

```
[ Laptop Battery Sensor ] ──> [ Python Script ] ──> [ Telegram API ] ──> [ Your Phone 📱 ]
```

1. The script periodically checks your battery state using `psutil`.
2. When the battery charge crosses key thresholds (e.g., **≤ 20%** or **≥ 80%**), it triggers an HTTP request to the Telegram Bot API.
3. You get a push notification instantly on your smartphone!

---

## 🚀 Quick Start

### Prerequisites

* **Python 3.x** installed on your laptop.
* A **Telegram** account.

### 1. Set Up Your Telegram Bot

1. Open Telegram and search for `@BotFather`.
2. Send `/newbot` and follow the on-screen instructions to create a bot.
3. Copy the **HTTP API Token** provided by BotFather.
4. Search for `@userinfobot` on Telegram and send any message to obtain your personal **Chat ID**.

### 2. Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/battery-notifier-bot.git
cd battery-notifier-bot
```

Install the required Python dependencies:

```bash
pip install psutil requests
```

### 3. Configuration

Open `Battery_Monitoring_TelegramBOT_IoT_Implementation.py` and insert your credentials:

```python
token = "PLACE_TOKEN_BOT_HERE"
chat_id = "YOUR_CHAT_ID"
```

### 4. Running the Application

Execute the script:

```bash
Battery_Monitoring_TelegramBOT_IoT_Implementation.py
```

---

## ⚙️ Running in the Background

### Windows
To run the script in the background without keeping a Command Prompt window open, rename your file extension from `.py` to `.pyw` and double-click it, or execute:

```bash
Battery_Monitoring_TelegramBOT_IoT_Implementation.py
```

*Tip: You can add a shortcut to this file in your Windows `Startup` folder (`shell:startup`) to start it automatically on boot.*

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome! Feel free to check the [issues page](https://github.com/Ryzn021/Laptop-Battery-Monitoring-through-Telegram-with-IoT/issues) if you have suggestions.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.
