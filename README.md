# AutoOps Suite 🚀

A comprehensive Python-based automation suite designed to streamline repetitive tasks such as file organization, web scraping, email automation, and system monitoring.

---

## 📌 Features

- 📁 Automated File Organizer (categorizes files by type)
- 🌐 Web Scraper (extracts data from websites using BeautifulSoup)
- 📧 Email Automation (SMTP-based email sender with templates)
- 🖥️ System Monitor (tracks CPU, memory, and disk usage)

---

## 🛠️ Tech Stack

- Python
- Libraries: os, shutil, requests, smtplib, psutil, BeautifulSoup
- Modular Architecture

---

## ⚙️ Project Structure
autoops-suite/
│── main.py
│── requirements.txt
│── README.md
│
├── modules/
│ ├── file_organizer.py
│ ├── web_scraper.py
│ ├── email_automation.py
│ └── system_monitor.py
│
├── data/
├── logs/
├── config/


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
📊 Output
Files automatically organized into folders
Scraped data printed from websites
Email automation triggered (SMTP-based)
Real-time system stats displayed
⚠️ Note

Email functionality may require Gmail App Password due to security restrictions.

👩‍💻 Author

Lakshmi Hasa