import pyautogui
import time
import keyboard
import tkinter as tk
from threading import Thread


class MouseMover:
    def __init__(self, move_distance=1000, interval=0.1):
        self.move_distance = move_distance
        self.interval = interval
        self.is_active = False
        self.toggle_key = 'ctrl+shift+m'  # You can change this to your preferred keystroke
        self.root = None
        self.status_label = None

    def toggle_mover(self):
        self.is_active = not self.is_active
        self.update_status()
        if self.is_active:
            Thread(target=self.move_mouse).start()

    def move_mouse(self):
        while self.is_active:
            current_x, current_y = pyautogui.position()
            pyautogui.moveRel(self.move_distance, 0, duration=0.1)
            time.sleep(0.1)
            pyautogui.moveRel(-self.move_distance, 0, duration=0.1)
            time.sleep(self.interval)

    def update_status(self):
        if self.status_label:
            status = "Active" if self.is_active else "Inactive"
            color = "green" if self.is_active else "red"
            self.status_label.config(text=f"Mouse Mover is {status}", fg=color)

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Mouse Mover Status")
        self.root.geometry("300x100")
        self.root.attributes('-topmost', True)

        self.status_label = tk.Label(self.root, text="Mouse Mover is Inactive", fg="red", font=("Arial", 14))
        self.status_label.pack(expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.is_active = False
        self.root.destroy()

    def run(self):
        keyboard.add_hotkey(self.toggle_key, self.toggle_mover)
        self.create_gui()
        self.root.mainloop()


if __name__ == "__main__":
    mover = MouseMover()
    mover.run()
