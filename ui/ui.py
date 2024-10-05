import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from products.products import Products


class Ui():
    def __init__(self):
        self.windows = Tk()
        self.windows.geometry("1156x834")
        self.windows.title("Excel para o Banco")
        self.windows.config(background="#080121")
        self.conts = 0
        self.products = Products()
        self.frame1()
        self.buttonPainel()
        self.canvasImage()
        self.firma()
        self.clearLIstEntrys()
        self.ioMainLoop()

        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=820, y=791, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=251, height=276,
                                   background="#4A1985")
        self.anchorPane.place(x=55, y=64) 
        
          
        label_finura = tk.Label(self.anchorPane, text="Finura:", font=("Helvetica", 21),
                                bg="#4A1985")
        label_finura.place(x=20, y=182, width=90, height=31)
        
        self.label_agulha = tk.Label(self.anchorPane, text="Agulha:",
                                     font=("Helvetica", 21), bg="#4A1985")
        self.label_agulha.place(x=19, y=225, width=95, height=31)

        self.finuraEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.finuraEntry.place(x=120, y=185, width=81, height=26)

        self.agulhaEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.agulhaEntry.place(x=120, y=228, width=81, height=26)
        
        combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell",
                                    "Jacquard", "ketten"], font=("Helvetica", 14),
                                   background= "#A580CA", foreground="#A580CA")
        combo_setor.place(x=21, y=92, width=87, height=25)
        combo_setor.set("Setor")

        
    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=406, height=400, background="#080121")
        image_frame.place(x=742, y=378)
        self.logo_img = PhotoImage(file= self.randomImagem())
        image_frame.create_image(100, 100, image = self.logo_img)
        
    def randomImagem(self):
        path = self.products.randImage()
        return path
                                       
              
    def buttonPainel(self):
        button_pane = tk.Frame(self.windows, width=334, height=114, background="#4A1985")
        button_pane.place(x=55, y=352)

        button_add = tk.Button(button_pane, text="Adicionar", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        button_add.place(x=179, y= 58, width=149)

        button_skip_turn = tk.Button(button_pane, text="Pular turno",
                                     font=("Helvetica", 18),
                                     bg="#A580CA", command= self.popADD)
        button_skip_turn.place(x=6, y=58)

        button_add_more = tk.Button(button_pane, text="Adicionar + ",
                                    font=("Helvetica", 18),
                                    bg="#A580CA",command= self.popADD)
        button_add_more.place(x=179, y=7)
     
    def comboxSheet(self):
        self.combo_setor = ttk.Combobox(self.anchorPane, values=["Uma panilha",
                                        "Varias"],
                                   font=("Helvetica", 14))
        self.combo_setor.place(x=21, y=92, width=87, height=25)
        self.combo_setor.set("Uma panilha")

            
    def popValueError(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Valor invalido",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        #self.dayEntry.delete(0, END)
        #self.monthEntry.delete(0, END)
        self.listData = []
        self.contsAdd = 0
            
        
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Error para Adicionar")
                               
        
    def clearLIstEntrys(self):
        self.listData = []
        self.finuraEntry.delete(0, END)
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
        
    def dayPopButton(self):
        popDia = Tk()
        popDia.geometry("300x200")
        popDia.config(background="#4A1985") 
        messagebox = tk.Label(master= popDia, text= "Digite o dia:",
                            font=("Helvetica", 14), bg="#4A1985")
        messagebox.pack(padx= 2, pady= 20) 
        
        combo_setor = ttk.Combobox(popDia, values=["Uma panilha", "Varias panilhas"],
                                   font=("Helvetica", 14), background= "#A580CA")
        combo_setor.place(x=105, y= 115, width=87, height=25)
        combo_setor.set("Uma panilha")
        
        button_ok = tk.Button(popDia, text="Iniciar",font=("Helvetica", 18),
                                        bg="#A580CA",command= self.popADD)
        button_ok.place(x= 105 , y= 155, width= 88, height= 35)
        
        self.diaGraficoEntry1 = tk.Entry(master= popDia)     
        self.diaGraficoEntry1.pack(padx= 6, pady= 2)
         
    def popADD(self):
        pass 

    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    