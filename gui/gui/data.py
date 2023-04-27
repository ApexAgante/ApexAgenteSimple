from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Button, PhotoImage, Toplevel


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def data_page(host):
    Data(host)


class Data(Toplevel):
    def on_closing(self):
        self.quit()
        self.destroy()

    def __init__(self, host, *args, **kwargs):
        Toplevel.__init__(self, *args, *kwargs)
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
        self.canvas.create_rectangle(
            40.0,
            14.0,
            780.0,
            16.0,
            fill="#FF3131",
            outline=""
        )

        self.canvas.create_rectangle(
            40.0,
            427.0,
            780.0,
            429.0,
            fill="#FF4646",
            outline="")

        self.canvas.create_text(
            116.0,
            33.0,
            anchor="nw",
            text="View Data",
            fill="#FF4646",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            116.0,
            65.0,
            anchor="nw",
            text=f"Host {host}",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1)
        )

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(image=button_image_1,
                          borderwidth=0,
                          highlightthickness=0,
                          command=lambda: print("button_1 clicked"),
                          relief="flat")
        button_1.place(x=725.0,
                       y=36.0,
                       width=54.52947998046875,
                       height=57.048614501953125)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(image=button_image_2,
                          borderwidth=0,
                          highlightthickness=0,
                          command=lambda: print("button_2 clicked"),
                          relief="flat")
        button_2.place(x=41.154327392578125,
                       y=35.52082824707031,
                       width=54.52947998046875,
                       height=57.04859924316406)

        self.canvas.create_rectangle(
            40.0,
            101.0,
            780.0,
            405.0,
            fill="#EFEFEF",
            outline=""
        )
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(False, False)
        self.mainloop()
