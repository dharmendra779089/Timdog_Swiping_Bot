# 🐶 Tindog Auto-Swiper Bot

An automated Python script powered by Selenium WebDriver that logs into the [Tindog](https://app.100daysofpython.dev/services/tindog/) web application and automatically "likes" dog profiles. 

This project demonstrates advanced browser automation techniques, including handling multiple popup windows, bypassing overlapping UI elements, and gracefully handling dynamic loading delays.

## ✨ Features

* **Multi-Window Navigation:** Automatically detects, switches to, and logs in through a separate "Facebark" OAuth popup window before returning to the main application.
* **Intelligent Popup Handling:** Detects and dismisses intrusive system popups (Location, Notifications, Cookies) to clear the screen before swiping.
* **Automated Swiping Loop:** Automatically clicks the "Like" (heart) button for 20 consecutive profiles.
* **Match Interruption Recovery:** Uses Selenium's `ElementClickInterceptedException` to detect when an "It's a Match!" popup covers the screen, safely closing it and resuming the swiping loop without crashing.

## 🛠️ Prerequisites

To run this script on your local machine, you will need:
* **Python 3.7+** installed.
* **Google Chrome** browser installed.
* An active internet connection.

*(Note: Because this project uses Selenium 4, you do not need to manually download or configure a `chromedriver.exe`. The script handles browser initialization automatically.)*

## 🚀 Installation & Setup

1. **Clone or download this repository:**
   ```bash
   git clone [https://github.com/YourUsername/tindog-swiper-bot.git](https://github.com/YourUsername/tindog-swiper-bot.git)
   cd tindog-swiper-bot
   ```

2. **Install the required dependencies:**
   Run the following command to install the Selenium library:
   ```bash
   pip install selenium
   ```

3. **Configure your credentials:**
   Open `main.py` in your code editor and ensure the environment variables at the top of the file match your specific Tindog URL and fake Facebark test account details:
   ```python
   TINDOG_URL = "YOUR_PERSONAL_TINDOG_LINK_HERE"
   FACEBARK_EMAIL = "your_test_email@gmail.com"
   FACEBARK_PASSWORD = "your_test_password"
   ```

## 🎮 How to Run

Execute the script from your terminal:

```bash
python main.py
```

Sit back and watch the browser open, log in, clear the popups, and swipe right on all the good boys and girls!

## 🧠 Technical Highlights (Under the Hood)

* **`driver.window_handles`:** Used to track and switch focus between the main Tindog window `[0]` and the Facebark login modal `[1]`.
* **`try / except` Blocks:** The swiping loop is wrapped in nested exception handlers. If a profile loads too slowly (`NoSuchElementException`), the bot sleeps and tries again. If a Match popup blocks the like button (`ElementClickInterceptedException`), the bot intercepts the error, clicks the 'Keep Swiping' button, and continues seamlessly.
* **Targeting Strategies:** Uses a mix of XPath, CSS Selectors, Class Names, and IDs to accurately target dynamic React/web elements.

## ⚠️ Disclaimer

This script was built for educational purposes as part of a Python automation portfolio to demonstrate web scraping, DOM interaction, and error handling.
