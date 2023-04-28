import tkinter as tk
from app.gui.gui.login.gui import login_window
# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window

# ASSETS_PATH = Path(f"{os.getcwd()}/app/test/gui/assets")
# logo = tk.PhotoImage(file=ASSETS_PATH / "trend.png")
# print(logo)
# root.call('wm', 'iconphoto', root._w, logo)

if __name__ == "__main__":
    login_window(root)
    root.mainloop()
