import psutil
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        pass

    def get_stats(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        stats = {
            "CPU Usage": f"{cpu}%",
            "Memory Usage": f"{memory.percent}%",
            "Disk Usage": f"{disk.percent}%",
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return stats

    def display(self):
        stats = self.get_stats()

        print("\n🖥️ SYSTEM MONITOR\n")
        for key, value in stats.items():
            print(f"{key}: {value}")