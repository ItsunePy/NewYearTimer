import datetime, time
import customtkinter as ctk
from threading import Thread
from PIL import Image
from requests import get
import os

def refresh():
    while True:
        now = datetime.datetime.now()
        NY = datetime.datetime(2024, 1 ,1)
        d = NY - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        text_label.configure(text='{}   :   {}   :   {}   :   {}'.format(d.days, hh, mm, ss))
        time.sleep(1)

def closewindow(event):
    Timer.destroy()
    exit()

def hide(event):

    move.destroy()

    text_1.place(relx=0.5, rely=0.35, anchor="center")
    text_label.place(relx=0.5, rely=0.5, anchor="center")
    text.place(relx=0.5, rely=0.65, anchor="center")

    Timer.wm_attributes("-transparentcolor", "gray8")
    Timer.overrideredirect(True)

    bglabel.place(relx=0.5, rely=0.5, anchor="center")
    Timer.bind("<F2>", closewindow)

try: os.mkdir('images')
except FileExistsError: pass
try:
    with open('images\\nybg.png', 'xb') as f:
        icourl = get('https://raw.githubusercontent.com/ItsunePy/NewYearTimer/master/images/nybg.png').content
        f.write(icourl)
except FileExistsError: pass

Timer = ctk.CTk()
Timer.attributes("-topmost", True)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
Timer.title("Таймер до нг")
Timer.geometry("250x200")
Timer.resizable(False, False)

bg = ctk.CTkImage(dark_image=Image.open('images\\nybg.png'), size=(250, 250))
bglabel = ctk.CTkLabel(master=Timer, image=bg, text="", bg_color='gray8')

move = ctk.CTkLabel(master=Timer, text='Переместите виджет\nв удобное место\n\nЧтобы скрыть текст\nнажмите F2\n\nЧтобы закрыть виджет\nещё раз нажмите F2', font=('Minecraft Rus', 16), width=250, height=200, bg_color='black')
Timer.bind("<F2>", hide)
move.place(relx=0.5, rely=0.5, anchor="center")

text_1 = ctk.CTkLabel(master=Timer, text='До нового года осталось:', font=('Minecraft Rus', 14), width=200, bg_color='black')
text_label = ctk.CTkLabel(master=Timer, font=('Minecraft Rus', 20), width=200, bg_color='black')
text = ctk.CTkLabel(master=Timer, text='дней | часов | минут | секунд', font=('Minecraft Rus', 13), width=200, bg_color='black')

Thread(target=refresh, daemon=True).start()

Timer.mainloop()
