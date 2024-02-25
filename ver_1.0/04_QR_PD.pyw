from tkinter import *
import qrcode
from PIL import Image, ImageTk

# root:---
root = Tk()
root.geometry("600x600")
root.title("QR code Creator-Contact")
root.config(bg="#AE445A")

# variables:---
name_var = StringVar()
phone_var = StringVar()
email_var = StringVar()

# myFrame widgets ---

# nombre
lblName = Label(root, text="Nombre: ", bg="#F39F5A")
lblName.grid(row=1, column=1)
entryName = Entry(root, textvariable=name_var, bg="#662549", fg="white", font=("Helvetica"))
entryName.grid(row=1, column=2)

# teléfono
lblPhone = Label(root, text="Teléfono: ", bg="#F39F5A")
lblPhone.grid(row=2, column=1)
entryPhone = Entry(root, textvariable=phone_var, bg="#662549", fg="white", font=("Helvetica"))
entryPhone.grid(row=2, column=2)

# correo electrónico
lblEmail = Label(root, text="Correo electrónico: ", bg="#F39F5A")
lblEmail.grid(row=3, column=1)
entryEmail = Entry(root, textvariable=email_var, bg="#662549", fg="white", font=("Helvetica"))
entryEmail.grid(row=3, column=2)


# button function:---
def print_QR_contact():
    contact_info = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name_var.get()}\nTEL:{phone_var.get()}\nEMAIL:{email_var.get()}\nEND:VCARD"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(contact_info)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0077B5", back_color="white")
    img.save("qr_contact.png")

    # image + Image_Label
    image = Image.open("qr_contact.png")
    photo = ImageTk.PhotoImage(image)

    lblImage = Label(root, image=photo)
    lblImage.place(x=15, y=120)
    lblImage.image = photo


# btn widget:-crear QR code-IMG--
btnCreate = Button(root, text="Crear código QR de contacto", command=print_QR_contact, bg="#F29CA3")
btnCreate.grid(row=4, column=1)

# close root:---
root.mainloop()
