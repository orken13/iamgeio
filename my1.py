import tkinter
from curses.textpad import Textbox

from numba.core.compiler_machinery import pass_info

#form=tkinter.Tk()
#form.title("Başlık")
#form.minsize(width=500,height=700)

#label=tkinter.Label(
 #   text="merhaba Dunya"
#)

#def click_button():
    #em=entry_input.get()
  #  print(em)
#label.pack()
#label.config(text="selam",bg="black",fg="white",font=('arial',30,"italic"))
#label.pack()
#entry_input=tkinter.Entry(width=80)# input
#entry_input.pack()



#def fonk():
 #   print("selam millet")
#button1=tkinter.Button(text="BAŞLA",fg="yellow",bg="red",command=fonk)


#button1.grid(row=0,column=0)


#button1.pack()




##################

#import tkinter
#form=tkinter.Tk()
#form.title("baslık")
#def yaz():
 #   text_input.get()
#text_input=tkinter.Entry(width=80,bg='black',fg="white")
#text_input.pack()
#button=tkinter.Button(text="GEÇ", width=30,height=3,command=yaz,bg="red",fg="white")
#button.pack(side="left")#top yukarı,bottom aşağı
#button.place(x=225,y=0)
#button.pack()


def fonk():
    pass


button=tkinter.Button(command=fonk,text="giriş",bg="white")
button.config(padx=10 ,pady=20)
button.pack()
metin=Text(width=30)
metin.pack()












form.mainloop()


