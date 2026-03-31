from modules.gui import AutoOpsGUI
import tkinter as tk
import os

# Ensure folders exist
os.makedirs("data/source", exist_ok=True)
os.makedirs("data/organized", exist_ok=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoOpsGUI(root)
    root.mainloop()