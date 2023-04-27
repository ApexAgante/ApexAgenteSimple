from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel, messagebox
from gui.controller import check_user
from gui.gui.data import data_page


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def welcome():
    Welcome()


class Welcome(Toplevel):

    def welcomeFunc(self):
        if check_user(self.host.get()):
            user = self.host.get()
            self.on_closing()
            data_page(user)
            return
        else:
            messagebox.showerror(
                title="Invalid Hostname",
                message="Hostname doesn't exist",
            )

    def on_closing(self):
        self.quit()
        self.destroy()

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('Welcome to Apex Agente')
        self.geometry("820x465")
        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=465,
            width=820,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.canvas.create_image(
            683.5,
            144.5,
            image=entry_image_1
        )
        self.host = Entry(self.canvas,
                          bd=0,
                          bg="#EAEAEA",
                          fg="#000716",
                          highlightthickness=0)
        self.host.place(x=579.0,
                        y=131.0,
                        width=209.0,
                        height=25.0)
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(self.canvas,
                          image=button_image_1,
                          borderwidth=0,
                          highlightthickness=0,
                          command=self.welcomeFunc,
                          relief="flat")
        button_1.place(x=576.0, y=403.0, width=216.0, height=41.0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            550.0,
            465.0,
            fill="#FF4646",
            outline="")

        self.canvas.create_text(
            41.0,
            70.0,
            anchor="nw",
            text="Welcome to ApexAgente",
            fill="#FFFFFF",
            font=("MontserratRoman ExtraBold", 30 * -1)
        )

        self.canvas.create_rectangle(
            41.0,
            117.0,
            137.0,
            129.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            41.0,
            147.0,
            anchor="nw",
            text="We are a website that handle apex agent.",
            fill="#FFFFFF",
            font=("MontserratRoman Regular", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            170.0,
            anchor="nw",
            text="The way we work is to search through",
            fill="#FFFFFF",
            font=("MontserratRoman Regular", 18 * -1)
        )

        self.canvas.create_text(
            41.0,
            193.0,
            anchor="nw",
            text="hostname.",
            fill="#FFFFFF",
            font=("MontserratRoman Regular", 18 * -1)
        )

        self.canvas.create_text(
            599.0,
            77.0,
            anchor="nw",
            text="Enter credential",
            fill="#FF3131",
            font=("MontserratRoman Bold", 18 * -1)
        )

        self.canvas.create_text(
            580.0,
            117.0,
            anchor="nw",
            text="Host name",
            fill="#FF3131",
            font=("MontserratRoman Bold", 10 * -1)
        )

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.host.bind("<Return>", lambda x: self.welcomeFunc())
        self.mainloop()

