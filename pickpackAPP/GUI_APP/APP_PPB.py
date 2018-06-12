import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       def option_changed(self,*args):
           
           if("{}".format(variable.get())=="Stop"):
               if messagebox.askokcancel('Confirm selection', "Do you want to STOP receiving the information?" ):               
                   var.set("Stop working")
                   label.pack()               
               else:                   
                   label.pack()
                   self.destroy()                       
           else:
               if messagebox.askokcancel('Confirm selection', "You want to print from {}".format(variable.get())):                
                   var.set("You are typing information from {}".format(variable.get()))
                   label.pack()           
               else:                 
                   label.pack()
                   
       OPTIONS = [
       "Stop",
       "Packer A",
       "Packer B",
       "Packer C",
       "Packer D"
       ] #etc

       variable = StringVar(self)
       variable.set("select") # default value
       variable.trace("w", option_changed)
        
       w = Label(self, text="Please select a channel.",fg="black",height=4)
       w.pack()
        
       w = OptionMenu(self, variable,*OPTIONS)
       w.pack(fill=X,ipadx=200,padx=100)
        
       var = StringVar()
       label = Label( self, textvariable=var,fg="green",height=2 )
        
       var.set("You did not choose Data Channel")
       label.pack()
   
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label_pa1 = Label(self, text="Packer A ")
       label_pa1.grid(column=0, row=0)
       vara = StringVar()
       txt_pa1 = Entry(self,textvariable=vara,width=40)
       txt_pa1.grid(column=1, row=0)
       with open("packerA_URL.txt", "r", encoding='utf-8') as a:
               vara.set(a.read())
       def clicked_pa():
           #res = "Packer A URL =" + txt.get()
           if messagebox.askokcancel('Confirm settings', "Do you want to SAVE the new URL?" ):               
              f = open('packerA_URL.txt','w')           
              f.write(txt_pa1.get())
              f.close()
              label_pa2.configure(text= "Saved")             
           else:                   
              with open("packerA_URL.txt", "r", encoding='utf-8') as a:
                  vara.set(a.read())
           
           
       btn_pa1 = Button(self, text="SAVE", command=clicked_pa)
       btn_pa1.grid(column=2, row=0)
       
       label_pa2 = Label(self, text="",width=35)
       label_pa2.grid(column=1, row=1)
       ######################################
       label_pb1 = Label(self, text="Packer B ")
       label_pb1.grid(column=0, row=2)
       varb = StringVar()
       txt_pb1 = Entry(self,textvariable=varb,width=40)
       txt_pb1.grid(column=1, row=2)
       with open("packerB_URL.txt", "r", encoding='utf-8') as b:
               varb.set(b.read())
       def clicked_pb():
           #res = "Packer A URL =" + txt.get()
           
           if messagebox.askokcancel('Confirm settings', "Do you want to SAVE the new URL?" ):               
              f = open('packerB_URL.txt','w')           
              f.write(txt_pb1.get())
              f.close()
              label_pb2.configure(text= "Saved")             
           else:                   
              with open("packerB_URL.txt", "r", encoding='utf-8') as b:
                  varb.set(b.read())
           
       btn_pb1 = Button(self, text="SAVE", command=clicked_pb)
       btn_pb1.grid(column=2, row=2)
       label_pb2 = Label(self, text="",width=35)
       label_pb2.grid(column=1, row=3)
       ######################################
       label_pc1 = Label(self, text="Packer C ")
       label_pc1.grid(column=0, row=4)
       varc = StringVar()
       txt_pc1 = Entry(self,textvariable=varc,width=40)
       txt_pc1.grid(column=1, row=4)
       with open("packerC_URL.txt", "r", encoding='utf-8') as c:
               varc.set(c.read())
       def clicked_pc():
           #res = "Packer A URL =" + txt.get()
           if messagebox.askokcancel('Confirm settings', "Do you want to SAVE the new URL?" ):               
              f = open('packerC_URL.txt','w')           
              f.write(txt_pc1.get())
              f.close()
              label_pc2.configure(text= "Saved")             
           else:                   
              with open("packerC_URL.txt", "r", encoding='utf-8') as c:
                  varc.set(c.read())
           
       btn_pc1 = Button(self, text="SAVE", command=clicked_pc)
       btn_pc1.grid(column=2, row=4)
       label_pc2 = Label(self, text="",width=35)
       label_pc2.grid(column=1, row=5)
       ######################################
       label_pd1 = Label(self, text="Packer D ")
       label_pd1.grid(column=0, row=6)
       vard = StringVar()
       txt_pd1 = Entry(self,textvariable=vard,width=40)
       txt_pd1.grid(column=1, row=6)
       with open("packerD_URL.txt", "r", encoding='utf-8') as d:
               vard.set(d.read())
       def clicked_pd():
           #res = "Packer A URL =" + txt.get()
           if messagebox.askokcancel('Confirm settings', "Do you want to SAVE the new URL?" ):               
              f = open('packerD_URL.txt','w')           
              f.write(txt_pd1.get())
              f.close()
              label_pd2.configure(text= "Saved")             
           else:                   
              with open("packerD_URL.txt", "r", encoding='utf-8') as d:
                  vard.set(d.read())
           
       btn_pd1 = Button(self, text="SAVE", command=clicked_pd)
       btn_pd1.grid(column=2, row=6)
       label_pd2 = Label(self, text="",width=35)
       label_pd2.grid(column=1, row=7)
       ########################################
       def clicked_reset():
           #res = "Packer A URL =" + txt.get()
           #label_pd2.configure(text= res)
           #txt.set("5555555555")
           label_pa2.configure(text= "")
           label_pb2.configure(text= "")
           label_pc2.configure(text= "")
           label_pd2.configure(text= "")
           with open("packerA_URL.txt", "r", encoding='utf-8') as a:
               vara.set(a.read())
           with open("packerB_URL.txt", "r", encoding='utf-8') as b:
               varb.set(b.read())
           with open("packerC_URL.txt", "r", encoding='utf-8') as c:
               varc.set(c.read())
           with open("packerD_URL.txt", "r", encoding='utf-8') as d:
               vard.set(d.read())
           
       btn_reset = Button(self, text="Reset defult", command=clicked_reset)
       btn_reset.grid(column=1, row=8)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       with open("about.txt", "r", encoding='utf-8') as f:
           Label(self, text=f.read()).pack()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Work space", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Seting API", command=p2.lift)
        b3 = tk.Button(buttonframe, text="About", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        
        p1.show()
   
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pickpack Bot")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry('350x250')
    
    root.mainloop()