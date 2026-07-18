# 18-07-2026
# Amaan Sajina
# Prodigy_CS_04 Keyboard Event Logger


import tkinter as tk
from tkinter import messagebox

LOG_FILE = "keystrokes.txt"

logging_enabled = True


#function to save pressed key
def log_key(event):

    if not logging_enabled:
        return

    key = event.keysym

    #handle special keys
    if key == "space":
        key = "[SPACE]"
    elif key == "Return":
        key = "[ENTER]"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif len(event.char) == 1:
        key = event.char

    with open(LOG_FILE, "a") as file:
        file.write(key + "\n")

    label.config(text=f"Last Key Pressed: {key}")


#start logging in local file
def start_logging_keys():
    global logging_enabled
    logging_enabled = True
    status.config(text="Status: Logging Enabled")


#stop logging in local file
def stop_logging_keys():
    global logging_enabled
    logging_enabled = False
    status.config(text="Status: Logging Disabled")


#clear local log file
def clear_logFile():

    with open(LOG_FILE, "w") as file:
        file.write("")

    messagebox.showinfo("Success", "Log file cleared.")


#exit application
def exit_program():
    window.destroy()


# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("Consent-Based Keyboard Event Logger")
window.geometry("600x450")

title = tk.Label(
    window,
    text="Consent-Based Keyboard Event Logger",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

info = tk.Label(
    window,
    text="Click inside this window and press keys. \nAll keys you pressed on keyboard are being recorded in log file. \nNote: Keys typed inside ONLY THIS window are being recorded.",
    font=("Arial", 11),
)
info.pack(pady=5)

status = tk.Label(
    window,
    text="Status: Logging Enabled",
    fg="green",
    font=("Arial", 11, "bold")
)
status.pack()

label = tk.Label(
    window,
    text="Last Key Pressed: None",
    font=("Arial", 12)
)
label.pack(pady=20)

start_button = tk.Button(
    window,
    text="Start Logging",
    width=20,
    command=start_logging_keys
)
start_button.pack(pady=5)

stop_button = tk.Button(
    window,
    text="Stop Logging",
    width=20,
    command=stop_logging_keys
)
stop_button.pack(pady=5)

clear_button = tk.Button(
    window,
    text="Clear Log File",
    width=20,
    command=clear_logFile
)
clear_button.pack(pady=5)

exit_button = tk.Button(
    window,
    text="Exit",
    width=20,
    command=exit_program
)
exit_button.pack(pady=15)

#listen for key presses event ONLY inside this window
window.bind("<Key>", log_key)

window.mainloop()