from tkinter import *
from PIL import ImageTk, Image

sai = Tk()
sai.title("Image")

imagenumber = 0

def forward():
    global my_label
    global button_front
    global button_back
    global imagenumber
    
    imagenumber = (imagenumber + 1) % len(image_list)
    
    my_label.grid_forget()
    my_label = Label(image=image_list[imagenumber])
    my_label.grid(row=0, column=0, columnspan=3)



def back():
    global my_label
    global button_front
    global button_back
    global imagenumber
    
    imagenumber = (imagenumber - 1) % len(image_list)
    
    my_label.grid_forget()
    my_label = Label(image=image_list[imagenumber])
    my_label.grid(row=0, column=0, columnspan=3)

image_paths = ["yogiAdithyanath.png", "modi.png", "car.gif", "donaldtrump.webp"]
image_list = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]

my_label = Label(image=image_list[imagenumber])
my_label.grid(row=0, column=0, columnspan=3)

button_exit = Button(sai, text="Exit", command=sai.destroy)
button_front = Button(sai, text="<<<", command=forward)
button_back = Button(sai, text=">>>", command=back)
button_rotate = Button(sai, text="Rotate", command=rotate)

button_exit.grid(row=1, column=0)
button_back.grid(row=1, column=1)
button_front.grid(row=1, column=2)
button_rotate.grid(row=1, column=3)

sai.mainloop()
