import tkinter as tk
from modules.file_organizer import FileOrganizer
from modules.web_scraper import WebScraper
from modules.system_monitor import SystemMonitor

class AutoOpsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoOps Suite 🚀")
        self.root.geometry("400x400")

        title = tk.Label(root, text="AutoOps Suite", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Buttons
        tk.Button(root, text="📁 Organize Files", command=self.run_file_organizer, width=30).pack(pady=5)
        tk.Button(root, text="🌐 Run Web Scraper", command=self.run_scraper, width=30).pack(pady=5)
        tk.Button(root, text="🖥️ System Monitor", command=self.run_monitor, width=30).pack(pady=5)

        self.output = tk.Text(root, height=10, width=45)
        self.output.pack(pady=10)

    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)

    def run_file_organizer(self):
        organizer = FileOrganizer("data/source", "data/organized")
        organizer.organize()
        self.log("✅ Files organized successfully")

    def run_scraper(self):
        scraper = WebScraper("https://news.ycombinator.com/")
        self.log("🌐 Scraping titles...")
        scraper.scrape_titles()
        self.log("✅ Scraping done")

    def run_monitor(self):
        monitor = SystemMonitor()
        stats = monitor.get_stats()
        self.log("🖥️ System Stats:")
        for k, v in stats.items():
            self.log(f"{k}: {v}")