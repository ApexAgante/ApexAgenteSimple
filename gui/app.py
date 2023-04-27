import tkinter as tk

from gui.gui.welcome import welcome
# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


def on_closing():
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()
    root.quit()


if __name__ == "__main__":

    welcome()
    # mainWindow()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
