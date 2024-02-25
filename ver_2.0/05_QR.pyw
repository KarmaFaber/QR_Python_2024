#colors MAIN ROOT---------------------------------------------------
#MainRoot: bg="#FAF0E6"x
#MainRoot bttns: bg="#B9B4C7", fg="#352F44"

#colors: SECONDARY ROOTS-------------------------------------------
#secondaryRoot QR with URL + Logo: bg="#FFB997"
#SecondaryRoots BTTNS: bg="#F67E7D", fg="#0B032D"

#secondaryRoot QR with PD: bg=#F0D9A2"
#SecondaryRoots BTTNS: bg="#AC7D88", fg="#44272E"
#----------------------------------------------------------------

#Pyhon modules------------------------------------------------------
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import qrcode
from PIL import Image, ImageTk
from qrcode import *

# main ROOT: opening------------------------------------------------
MainRoot=tk.Tk()
MainRoot.geometry("500x500")
MainRoot.title("Create QR Code.")
MainRoot.config(bg="#FAF0E6")

#button deffs:----------------------------------------------------
#deff of create QT button-----------------------------------------
def create_QR_URL():
  URL_root=Toplevel()
  URL_root.geometry("700x700")
  URL_root.title("QR code with URL")
  URL_root.config(bg="#FFB997")   

  #variables:
  #URL variable
  url_var=StringVar()
  # Color variables
  foreground_color_var = StringVar()
  background_color_var = StringVar()
  
  
  # text before Entry Box URL
  lblUrl=Label(URL_root, text="introduce your URL: ", bg="#FFB997")
  lblUrl.grid(row=1, column=1)

  # Entry Box URL
  entryBoxUrl=Entry(URL_root, textvariable=url_var, bg="#FFB997", fg="#0B032D", font=("Helvetica"))
  entryBoxUrl.focus()
  entryBoxUrl.grid(row=1, column=2)


  # text before Entry Box QR Color
  lblQrColor=Label(URL_root, text="introduce your QR color (RGB): ", bg="#FFB997")
  lblQrColor.grid(row=2, column=1)

  # Entry Box URL QR Color
  entryBoxColorQr=Entry(URL_root, textvariable=foreground_color_var, bg="#FFB997", fg="#0B032D", font=("Helvetica"))
  entryBoxColorQr.focus()
  entryBoxColorQr.grid(row=2, column=2)

  # text before Entry Box background QR Color
  lblBgColor=Label(URL_root, text="introduce your QR Background color (RGB): ", bg="#FFB997")
  lblBgColor.grid(row=3, column=1)

  # Entry Box URL background QR Color
  entryBoxBgColor=Entry(URL_root, textvariable=background_color_var, bg="#FFB997", fg="#0B032D", font=("Helvetica"))
  entryBoxBgColor.focus()
  entryBoxBgColor.grid(row=3, column=2)


  def create_qr_code(data, foreground_color, background_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    return qr_img
  
    
  def generate_qr_and_display():
    url = url_var.get()
    foreground_color = foreground_color_var.get()
    background_color = background_color_var.get()
    
    qr_img = create_qr_code(url, foreground_color, background_color)
    tk_img = ImageTk.PhotoImage(qr_img)

    qr_label.img = tk_img
    qr_label.config(image=tk_img)


  def save_as_Url():
    url_var=entryBoxUrl.get()
    foreground_color = foreground_color_var.get()
    background_color = background_color_var.get()
   
    qr_img=create_qr_code(url_var, foreground_color, background_color)

    #Save As generates QR image:
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    
    if file_name:
        qr_img.save(file_name)
  
 
  #preview button
  saveBttn=Button(URL_root, text="Generate and Preview QR", command=generate_qr_and_display, bg="#F67E7D", fg="#0B032D", font=("Helvetica"), height=1, width=40, relief="groove", borderwidth=5)
  saveBttn.grid(row=4, column=1)

  #save As button:
  saveBttn=Button(URL_root, text="Save As", command=save_as_Url, bg="#F67E7D", fg="#0B032D", font=("Helvetica"), height=1, width=40, relief="groove", borderwidth=5)
  saveBttn.grid(row=5, column=1)

  # Label to display the generated QR code image
  qr_label = tk.Label(URL_root)
  qr_label.grid(row=6, column=1, pady=10)


  URL_root.mainloop()
#secondary root URL -QR CODE ends------------------------------------------------------------------------------------
       
#def for bttn -> create QR with Personal Data starts here------------------------------------------------------------
def create_QR_PD():
  PD_root=Toplevel()
  PD_root.geometry("700x700")
  PD_root.title("QR code Contact information.")
  PD_root.config(bg="#F0D9A2")

  #variables:
  Name=StringVar()
  Number=StringVar()
  Email=StringVar()

  # Color variables
  foreground_color_var = StringVar()
  background_color_var = StringVar()

  nameLbl=Label(PD_root, text="Introduce your name: ", bg="#F0D9A2")
  nameLbl.grid(row=1, column=1)
  nameBox=Entry(PD_root, textvariable=Name, bg="#F0D9A2", fg="#56313A", font=("Helvetica"))
  nameBox.grid(row=1, column=2)

  NumberLbl=Label(PD_root, text="Introduce your Number: ", bg="#F0D9A2")
  NumberLbl.grid(row=2, column=1)
  NumberBox=Entry(PD_root, textvariable=Number, bg="#F0D9A2", fg="#56313A", font=("Helvetica"))
  NumberBox.grid(row=2, column=2)

  EmailLbl=Label(PD_root, text="Introduce your Email: ", bg="#F0D9A2")
  EmailLbl.grid(row=3, column=1)
  EmailBox=Entry(PD_root, textvariable=Email, bg="#F0D9A2", fg="#56313A", font=("Helvetica"))
  EmailBox.grid(row=3, column=2)

  QrColorLbl=Label(PD_root, text="Introduce your QR color: ", bg="#F0D9A2")
  QrColorLbl.grid(row=4, column=1)
  QrColorBox=Entry(PD_root, textvariable=foreground_color_var, bg="#F0D9A2", fg="#56313A", font=("Helvetica"))
  QrColorBox.grid(row=4, column=2)

  BGColorLbl=Label(PD_root, text="Introduce your QR Background color: ", bg="#F0D9A2")
  BGColorLbl.grid(row=5, column=1)
  BGColorBox=Entry(PD_root, textvariable=background_color_var, bg="#F0D9A2", fg="#56313A", font=("Helvetica"))
  BGColorBox.grid(row=5, column=2)


  #deffs:
  def create_QR_code(data, foreground_color, background_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    return qr_img
    

  def generate_qr_and_display():
    PD_data=f"BEGIN:VCARD\nVERSION:3.0\nFN:{Name.get()}\nTEL:{Number.get()}\nEMAIL:{Email.get()}\nEND:VCARD"
    foreground_color=foreground_color_var.get()
    background_color=background_color_var.get()

    qr_img=create_QR_code(PD_data, foreground_color, background_color)
    tk_img=ImageTk.PhotoImage(qr_img)

    qr_label.img=tk_img
    qr_label.config(image=tk_img)


  def save_as_PD():
    PD_data=f"BEGIN:VCARD\nVERSION:3.0\nFN:{Name.get()}\nTEL:{Number.get()}\nEMAIL:{Email.get()}\nEND:VCARD"
    foreground_color=foreground_color_var.get()
    background_color=background_color_var.get()

    qr_img=create_QR_code(PD_data, foreground_color, background_color)

    #Save As generates QR image:
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    
    if file_name:
        qr_img.save(file_name)


  #buttons:
  #preview button
  saveBttn=Button(PD_root, text="Generate and Preview QR", command=generate_qr_and_display, bg="#AC7D88", fg="#44272E", font=("Helvetica"), height=1, width=40, relief="groove", borderwidth=5)
  saveBttn.grid(row=6, column=1)

  #save As button:
  saveBttn=Button(PD_root, text="Save As", command=save_as_PD, bg="#AC7D88", fg="#44272E", font=("Helvetica"), height=1, width=40, relief="groove", borderwidth=5)
  saveBttn.grid(row=7, column=1)

  # Label to display the generated QR code image
  qr_label = tk.Label(PD_root)
  qr_label.grid(row=8, column=1, pady=10)
  

  PD_root.mainloop()
   

#buttons--------------------------------------------------------
#BTTNS create QR------------------------------------------------
#button create QR with URL-> color selection--------------------
btn_qr=Button(MainRoot,text="QR_URL", command=create_QR_URL, bg="#B9B4C7", fg="#352F44", font=("Helvetica"), borderwidth=5, height=2, width=30)
btn_qr.config(font=("Courtier",12))
btn_qr.grid(row=1,column=0)


#button create QR with Personal Data-> + color selection---------
btn_PD=Button(MainRoot,text="QR_Personal Data", command=create_QR_PD, bg="#B9B4C7", fg="#352F44", font=("Helvetica"), borderwidth=5, height=2, width=30)
btn_PD.config(font=("Courtier",12))
btn_PD.grid(row=2,column=0)


#closing main root:----------------------------------------------
MainRoot.mainloop()

