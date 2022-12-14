
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import customtkinter


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1268x799")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 799,
    width = 1268,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    317.0,
    347.0,
    image=image_image_1
)

canvas.create_text(
    233.0,
    702.0,
    anchor="nw",
    text="Proceed",
    fill="#000000",
    font=("GRANDGALAXY", 24 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    951.0,
    399.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=117.0,
    y=669.0,
    width=395.0,
    height=107.0
)

R = customtkinter.CTkSlider(master=window, from_=0, to=255, command=print("Hi"),width=500,border_width=0,progress_color="#9747FF",button_color="#672DB2",button_hover_color="#481E7E",fg_color="#D9D9D9")
R.place(x=700, y=254)
G = customtkinter.CTkSlider(master=window, from_=0, to=255, command=print("Hi"),width=500,border_width=0,progress_color="#9747FF",button_color="#672DB2",button_hover_color="#481E7E",fg_color="#D9D9D9")
G.place(x=700, y=306)
B = customtkinter.CTkSlider(master=window, from_=0, to=255, command=print("Hi"),width=500,border_width=0,progress_color="#9747FF",button_color="#672DB2",button_hover_color="#481E7E",fg_color="#D9D9D9")
B.place(x=700, y=358)
Brightness = customtkinter.CTkSlider(master=window, from_=0, to=255, command=print("Hi"),width=500,border_width=0,progress_color="#9747FF",button_color="#672DB2",button_hover_color="#481E7E",fg_color="#D9D9D9")
Brightness.place(x=700, y=504)
window.resizable(False, False)
window.mainloop()
