# main.py

import tkinter as tk
from gui import MathMemoryGame

def main():
    root = tk.Tk()
    app = MathMemoryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
