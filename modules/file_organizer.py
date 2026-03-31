import os
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

        self.categories = {
            "Documents": [".pdf", ".docx", ".txt"],
            "Images": [".jpg", ".png", ".jpeg"],
            "Videos": [".mp4", ".mkv"],
            "Code": [".py", ".js", ".html"]
        }

    def organize(self):
        for file in os.listdir(self.source):
            file_path = os.path.join(self.source, file)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()

                moved = False
                for category, extensions in self.categories.items():
                    if ext in extensions:
                        dest_folder = os.path.join(self.destination, category)
                        os.makedirs(dest_folder, exist_ok=True)

                        dest_path = os.path.join(dest_folder, file)

                        if os.path.exists(dest_path):
                            base, ext = os.path.splitext(file)
                            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                            file = f"{base}_{timestamp}{ext}"
                            dest_path = os.path.join(dest_folder, file)

                        shutil.move(file_path, dest_path)
                        moved = True
                        break

                if not moved:
                    other_folder = os.path.join(self.destination, "Others")
                    os.makedirs(other_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(other_folder, file))