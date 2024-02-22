#Pyhon modules------------------------------------------------------
from tkinter import *
import qrcode
from PIL import ImageTk, ImageTk

#myModules/ classes------------------------------------------------
#from MyModulesQR import *
#from MyModulesRoot import *


# main ROOT: opening------------------------------------------------
MainRoot=Tk()
MainRoot.geometry("800x800")
MainRoot.title("Create QR Code.")
MainRoot.config(bg="#FAF0E6")

#colors:------------------------------------------------------------
#MainRoot: bg="#FAF0E6"
#MainRoot bttns: bg="#B9B4C7", fg="#352F44"

#colors:
#secondaryRoots: bg=
#SecondaryRoots: bg="", fg=""
#----------------------------------------------------------------


#button deffs:----------------------------------------------------
#deff of create QT button-----------------------------------------
def create_QR_URL():
    
    print("create QR with URL")



#deff for bttn -> create QR with URL +Logo
def create_QR_Logo():
    print("create QR with URL+Logo")



#def for bttn -> create QR with URL -> BW QR code + LOGO
def create_QR_PD():
    print("create QR with PD")
   



#buttons--------------------------------------------------------
#BTTNS create QR------------------------------------------------
#button create QR with URL-> color selection--------------------
btn_qr=Button(MainRoot,text="QR_URL", command=create_QR_URL, bg="#B9B4C7", fg="#352F44")
btn_qr.config(font=("Courtier",12))
btn_qr.grid(row=1,column=0)


#button create QR with URL+ LOGO-> color and logo selection------
btn_logo=Button(MainRoot,text="QR: URL + Logo", command=create_QR_Logo, bg="#B9B4C7", fg="#352F44")
btn_logo.config(font=("Courtier",12))
btn_logo.grid(row=2,column=0)

#button create QR with Personal Data-> + color selection---------
btn_PD=Button(MainRoot,text="QR_Personal Data", command=create_QR_PD, bg="#B9B4C7", fg="#352F44")
btn_PD.config(font=("Courtier",12))
btn_PD.grid(row=3,column=0)


#closing main root:----------------------------------------------
MainRoot.mainloop()

