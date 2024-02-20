from tkinter import *
import qrcode
from PIL import Image, ImageTk

#root:---
root=Tk()
root.geometry("600x600")
root.title("QR code Creator-URL-Basic")
root.config(bg="#AE445A")

#variables:---
url_var=StringVar()

# myFrame witgets ---

# texto antes del cuadro de texto---
lblUrl=Label(root, text="introduce your URL: ", bg="#F39F5A")
lblUrl.grid(row=1, column=1)

# cuadro de texto
entryBox=Entry(root, textvariable=url_var, bg="#662549", fg="white", font=("Helvetica"))
entryBox.focus()
entryBox.grid(row=1, column=2)

#button function:---
def print_QR_image():
    url_var=entryBox.get()
    # url_var.set(entryBox.get()) otra opción de codigo


    # hacemos el QR core en imagen y guardamos:
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    # ERROR_CORRECT_L-About 7% or less errors can be corrected.
    # ERROR_CORRECT_M-(default)-About 15% or less errors can be corrected.
    # ERROR_CORRECT_Q-About 25% or less errors can be corrected.
    # ERROR_CORRECT_H-About 30% or less errors can be corrected.
    data = url_var
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0077B5", black_color="white")

    # Logo image path
    imagenLogo = r'D:\Programación_2024\Python_2024\QR_Python\ver_1.0\logo_GH.png'
    logo = Image.open(imagenLogo)

    # Calculate logo position
    qr_img_size = img.size
    logo_position = ((qr_img_size[0] - logo.size[0]) // 2, (qr_img_size[0] - logo.size[0]) // 2)

    # Paste the logo onto the QR code
    img.paste(logo, logo_position)

    img.save("qr_tkinter.png")



    #image + Image_Label
    image = Image.open("qr_tkinter.png")
    photo=ImageTk.PhotoImage(image)

    lblImage=Label(root, image=photo)
    lblImage.place(x=15, y=95)
    lblImage.image=photo



#btn witget:-crear QR code-IMG--
btnCreate=Button(root, text="Create QR code", command=print_QR_image, bg="#F29CA3")
btnCreate.grid(row=3, column=1)


#close root:---
root.mainloop()