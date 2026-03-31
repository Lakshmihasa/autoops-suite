from modules.file_organizer import FileOrganizer
import os

# create test folders
os.makedirs("data/source", exist_ok=True)
os.makedirs("data/organized", exist_ok=True)

if __name__ == "__main__":
    organizer = FileOrganizer("data/source", "data/organized")
    organizer.organize()

    print("✅ Files organized successfully!")