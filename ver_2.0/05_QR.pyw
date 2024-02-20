#Pyhon modules------------------------------------------------------
from tkinter import *
import qrcode
from PIL import ImageTk, ImageTk

#myModules----------------------------------------------------------




# main ROOT--------------------------------------------------------

MainRoot=Tk()
MainRoot.geometry("800x800")
MainRoot.title("Create QR Code.")
#root.config(codigo gradiente colores)




#deff's-------------------------------------------------------------
#DEFF'S create QR---------------------------------------------------
#def for bttn -> create QR with URL -> BW QR code
def crear_QR_BW():
    root_1 = Tk()
    root_1.geometry("600x600")
    root_1.title("QR code black and white")
    root_1.config(bg="#F39F5A")

    # URL variable
    url_var = StringVar()

    # texto antes del cuadro de texto---
    lblUrl = Label(root_1, text="introduce your URL: ", bg="#F39F5A")
    lblUrl.grid(row=1, column=1)

    #entry Box: URL
    entryBox = Entry(root_1, textvariable=url_var, bg="#662549", fg="white", font=("Helvetica"))
    entryBox.focus()
    entryBox.grid(row=1, column=2)

    #bttn deff
    def print_image_1():
        print("img_1")
    #bttn
    btnCreate = Button(root_1, text="Create QR code", command=print_image_1, bg="#F29CA3")
    btnCreate.grid(row=1, column=3)




    root_1.mainloop()

#def for bttn -> create QR with URL -> COLOR QR code
def crear_QR_Color():
    root_2 = Tk()
    root_2.geometry("600x600")
    root_2.title("QR code Color")
    root_2.config(bg="#F3845A")

    # URL variable
    url_var = StringVar()

    # texto antes del cuadro de texto---
    lblUrl = Label(root_2, text="introduce your URL: ", bg="#F39F5A")
    lblUrl.grid(row=1, column=1)

    #entry Box: URL
    entryBox = Entry(root_2, textvariable=url_var, bg="#662549", fg="white", font=("Helvetica"))
    entryBox.focus()
    entryBox.grid(row=1, column=2)

    #bttn deff
    def print_image_2():
        print("img_2")
    #bttn
    btnCreate = Button(root_2, text="Create QR code", command=print_image_2, bg="#F29CA3")
    btnCreate.grid(row=1, column=3)

    root_2.mainloop()

#def for bttn -> create QR with URL -> BW QR code + LOGO
def crear_QR_BW_Logo():
    root_3 = Tk()
    root_3.geometry("600x600")
    root_3.title("QR code Black and White with Logo")
    root_3.config(bg="#F3E05A")

    # URL variable
    url_var = StringVar()

    # texto antes del cuadro de texto---
    lblUrl = Label(root_3, text="introduce your URL: ", bg="#F39F5A")
    lblUrl.grid(row=1, column=1)

    #entry Box: URL
    entryBox = Entry(root_3, textvariable=url_var, bg="#662549", fg="white", font=("Helvetica"))
    entryBox.focus()
    entryBox.grid(row=1, column=2)

    #bttn deff
    def print_image_3():
        print("img_3")
    #bttn
    btnCreate = Button(root_3, text="Create QR code", command=print_image_3, bg="#F29CA3")
    btnCreate.grid(row=1, column=3)

    root_3.mainloop()

# def for bttn -> create QR with URL -> COLOR QR code + LOGO
def crear_QR_C_Logo():
    root_4 = Tk()
    root_4.geometry("600x600")
    root_4.title("QR code Color with Logo")
    root_4.config(bg="#E9DFF0")

    # URL variable
    url_var = StringVar()

    # texto antes del cuadro de texto---
    lblUrl = Label(root_4, text="introduce your URL: ", bg="#F39F5A")
    lblUrl.grid(row=1, column=1)

    #entry Box: URL
    entryBox = Entry(root_4, textvariable=url_var, bg="#662549", fg="white", font=("Helvetica"))
    entryBox.focus()
    entryBox.grid(row=1, column=2)

    #bttn deff
    def print_image_4():
        print("img_4")
    #bttn
    btnCreate = Button(root_4, text="Create QR code", command=print_image_4, bg="#F29CA3")
    btnCreate.grid(row=1, column=3)


    root_4.mainloop()

# def for bttn -> create QR with Personal Data -> BW QR code
def crear_QR_BW_PD():
    root_5 = Tk()
    root_5.geometry("600x600")
    root_5.title("QR code BW with Personal Data")
    root_5.config(bg="#F0DFE4")



    root_5.mainloop()

# def for bttn -> create QR with Personal Data -> COLOR QR code
def crear_QR_C_PD():
    root_6 = Tk()
    root_6.geometry("600x600")
    root_6.title("QR code Color with Personal Data")

    root_6.mainloop()

# def for bttn -> create QR with PDF -> BW QR code
def crear_QR_PDF():
    root_7 = Tk()
    root_7.geometry("600x600")
    root_7.title("QR code Color with PDF")

    root_7.mainloop()


#DEFF'S COLOR FORMAT TKINTER---------------------------------------------------
# def for bttn -> change panel color with RGB-chose 1 color
def color_p_RGB():
    root_8 = Tk()
    root_8.geometry("600x600")
    root_8.title("Change panel color with RGB")

    root_8.mainloop()

# def for bttn -> change panel color with RGB-chose 6 colors
def color_p_RGB_v():
    root_9 = Tk()
    root_9.geometry("600x600")
    root_9.title("Change panel color with RGB")

    root_9.mainloop()


# def for bttn -> change panel color with 1 color chooser:
def color_p_color():
    root_10 = Tk()
    root_10.geometry("600x600")
    root_10.title("Change panel color with colors chooser")

    root_10.mainloop()

# def for bttn -> change panel color with 6 colors chooser:
def color_p_color_v():
    root_11 = Tk()
    root_11.geometry("600x600")
    root_11.title("Change panel color with colors chooser")

    root_11.mainloop()


#buttons--------------------------------------------------------------
#BTTNS create QR-------------------------------------------------
#button create QR with URL-> B/W QR code------------------------------
btn_bw=Button(MainRoot,text="QR_URL_BN", command=crear_QR_BW, bg="#072E33", fg="#6DA5C0")
btn_bw.config(font=("Courtier",12))
btn_bw.grid(row=1,column=0)


#button create QR with URL-> COLOR QR code-----------------------------
btn_color=Button(MainRoot,text="QR_URL_Color", command=crear_QR_Color, bg="#072E33", fg="#6DA5C0")
btn_color.config(font=("Courtier",12))
btn_color.grid(row=2,column=0)

#button create QR with LOGO/URL-> BW QR code----------------------------
btn_bw_logo=Button(MainRoot,text="QR_URL_BN_Logo", command=crear_QR_BW_Logo, bg="#072E33", fg="#6DA5C0")
btn_bw_logo.config(font=("Courtier",12))
btn_bw_logo.grid(row=3,column=0)

#button create QR with LOGO/URL-> COLOR QR code-------------------------
btn_color_logo=Button(MainRoot,text="QR_URL_Color_Logo", command=crear_QR_C_Logo, bg="#072E33", fg="#6DA5C0")
btn_color_logo.config(font=("Courtier",12))
btn_color_logo.grid(row=4,column=0)

#button create QR with personal data-> BW QR code-----------------------
btn_bw_pd_bw=Button(MainRoot,text="QR_PersonalData_BN", command=crear_QR_BW_PD, bg="#072E33", fg="#6DA5C0")
btn_bw_pd_bw.config(font=("Courtier",12))
btn_bw_pd_bw.grid(row=5,column=0)


#button create QR with Personal data-> COLOR QR code--------------------
btn_bw_pd_color=Button(MainRoot,text="QR_PersonalData_Color", command=crear_QR_C_PD, bg="#072E33", fg="#6DA5C0")
btn_bw_pd_color.config(font=("Courtier",12))
btn_bw_pd_color.grid(row=6,column=0)


#button create QR with PDF ---------------------------------------------
btn_pdf=Button(MainRoot,text="QR_PDF", command=crear_QR_PDF, bg="#072E33", fg="#6DA5C0")
btn_pdf.config(font=("Courtier",12))
btn_pdf.grid(row=7,column=0)

#----------------------------------------------------------------------------
#BTTNS tkinter format-COLORS-------------------------------------------------
#elegir 1 color con datos RGB:
btn_panel_c=Button(MainRoot,text="Cambiar de color al panel_RGB_1 color", command=color_p_RGB, bg="#072E33", fg="#6DA5C0")
btn_panel_c.config(font=("Courtier",12))
btn_panel_c.grid(row= 1,column=1)


#elegir 6 colores con datos RGB:
btn_panel_c_v=Button(MainRoot,text="Cambiar de color al panel_RGB_6 colores", command=color_p_RGB_v, bg="#072E33", fg="#6DA5C0")
btn_panel_c_v.config(font=("Courtier",12))
btn_panel_c_v.grid(row= 2,column=1)


#elegir 1 color con seleccionador:
btn_panel_c_2=Button(MainRoot,text="Seleccionar 1 color Gradientes", command=color_p_color, bg="#072E33", fg="#6DA5C0")
btn_panel_c_2.config(font=("Courtier",12))
btn_panel_c_2.grid(row=3,column=1)

#elegir 6 colores con seleccionador:
btn_panel_c_2=Button(MainRoot,text="Seleccionar 6 colores Gradientes", command=color_p_color_v, bg="#072E33", fg="#6DA5C0")
btn_panel_c_2.config(font=("Courtier",12))
btn_panel_c_2.grid(row=4,column=1)


MainRoot.mainloop()

