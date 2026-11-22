import tkinter as tk
import random

windows = []
running = True

MESSAGES = [
    "JEŻ ZAATAKOWAŁ KOMPUTER 🦔",
    "ERROR 666",
    "ZA DUŻO JEŻY!!!",
    "KOLCE DETECTED",
    "JEZ.EXE",
    "SYSTEM NIE ŻYJE",
    "GDZIE JEST MÓJ JEŻ?",
    "🦔🦔🦔🦔🦔"
]

COLORS = [
    "red", "blue", "purple",
    "green", "orange", "magenta"
]

root = tk.Tk()
root.withdraw()

def spawn():
    if not running or len(windows) >= 60:
        return

    win = tk.Toplevel()
    win.title(random.choice(["ERROR", "JEZ.EXE", "VIRUS", "ALERT!!!"]))

    w = random.randint(200, 350)
    h = random.randint(120, 200)

    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()

    x = random.randint(0, max(0, sw-w))
    y = random.randint(0, max(0, sh-h))

    win.geometry(f"{w}x{h}+{x}+{y}")

    color = random.choice(COLORS)
    win.configure(bg=color)

    tk.Label(
        win,
        text=random.choice(MESSAGES),
        font=("Arial", 16, "bold"),
        fg="white",
        bg=color,
        wraplength=w-20
    ).pack(expand=True)

    tk.Label(
        win,
        text="🦔 🦔 🦔",
        font=("Arial", 22),
        bg=color
    ).pack()

    windows.append(win)

    win.protocol(
        "WM_DELETE_WINDOW",
        lambda w=win: close_window(w)
    )

    if running:
        root.after(random.randint(150, 450), spawn)

def close_window(win):
    if win in windows:
        windows.remove(win)
    win.destroy()

def stop(event=None):
    global running
    running = False

    for win in windows[:]:
        try:
            win.destroy()
        except tk.TclError:
            pass

    root.destroy()

root.bind_all("<Escape>", stop)

# START!
spawn()

root.mainloop()