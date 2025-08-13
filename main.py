from tkinter import *
import requests

def get_quote():

    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Me Says")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

aristo_marx_img = PhotoImage(file="aristo_marx (1).png")
am_button = Button(image=aristo_marx_img, highlightthickness=0, command=get_quote)
am_button.grid(row=1, column=0)


window.mainloop()