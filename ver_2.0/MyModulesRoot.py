import tkinter as Tk


# Root Creator Classes-----------------------------
class SecondaryRootURL:
    def __init__(self, color_BG_Secondary_Root, color_Bttns, color_Bttns_f, SR_title, SR_geometry, bttn_p_text, row_b, column_b):
    # variebles pendientes de meter: color_QR, color_BG_QR, logo, color_lbl_f, color_entryBox_f, URL_dir, ??? bttn_p_grid, button_p_command,
        
        #color variables: Secondary ROOT
        self.color_BG_Secondary_Root=color_BG_Secondary_Root  #Secondary Root color
        
        # Secondary Root config variables
        self.SR_title=SR_title  #secondary Root Title
        self.SG_geometry=SR_geometry 

        # secondary Root config: 
        self.secondary_Root=Tk.Tk() #secondary Root variable
        self.secondary_Root.config(bg=color_BG_Secondary_Root)  #secondary Root BG color aplication
        self.secondary_Root.title(SR_title) #secondary Root title
        self.secondary_Root.geometry(SR_geometry) #secondary Root geometry- tamaño de la Root

        #buttons:
        self.color_Bttns=color_Bttns #Secondary Root Buttons color
        self.color_Bttns_f=color_Bttns_f #Secondary Root Buttons fuent color
        self.bttn_p_text=bttn_p_text
        #self.bttn_p_grid=bttn_p_grid
        self.row_b=row_b
        self.column_b=column_b
        
        #self.button_p_command=button_p_command

        #bttn Preview:
        #def button_p_command_def(self):
         #   print("bttn 1 doing things")
        
        #command=button_p_command_def,
        
        self.Btn_Preview=Tk.Button(SecondaryRootURL, bttn_p_text, bg=color_Bttns, fg=color_Bttns_f)
        self.Btn_Preview.grid(row=row_b, column=column_b)

        


        self.secondary_Root.mainloop() #clossing Root


    
    def create_secondary_Root(self):
        new_root=Tk()
        return new_root
    
    

        
        
        






#class SecondaryRootUrlLogo():


#class SecondaryRootUrlPd():




#class MyRootColors:

    #atributos/variable:
   


    #metodos o funciones:
   



    #print("helo colors")
