import tkinter as tk
from datetime import datetime
root = tk.Tk()
root.title("Current date")
today_date=datetime.now().strftime("%A %d %B %Y")
label = tk.Label(root, text=today_date)
font =("times new roman", 20)
label.pack(padx=5, pady=5)
root.mainloop()