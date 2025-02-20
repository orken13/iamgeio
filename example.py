import tkinter



form=tkinter.Tk()

form.title("Vucüt kitle İndeks durum")

form.minsize(width=500,height=400)
label1=tkinter.Label(text="kilo",background="yellow",foreground="black",width=20,height=2)
label1.pack(padx=20,pady=20)
entry1=tkinter.Entry()
entry1.pack(padx=10,pady=30)
label2=tkinter.Label(text="boy",background="yellow",foreground="black",width=20,height=2)
label2.pack(padx=20,pady=30)
entry2=tkinter.Entry()
entry2.pack(padx=20,pady=30)
def hesap():
    a=int(entry1.get())
    b=float(entry2.get())
    index= a/(b**2)
    label3.config(text=index)
    if index < 18.5:
         print("under weight")
    if index > 18.5 and index < 24.9 :
       label4.config(text="normal")
    if index > 25 and index < 29.9 :
       label4.config(text="over weight")
    if index > 30 and index < 34.9 :
       label4.config(text="Obesity (class 1)")
    if index > 35 and index < 39.9 :
       label4.config(text="Obesity (class 2)")
    if index > 40 :
       label4.config(text="Extreme Obesity")

buton1=tkinter.Button(text="hesapla",command=hesap,background="red",foreground="black",width=20,height=2)
buton1.pack(padx=10,pady=10)

label3=tkinter.Label(text="sonuc",background="pink",foreground="black",width=20,height=2)
label3.pack(padx=10,pady=20)
label4=tkinter.Label(text="BMI",background="black",foreground="white",width=20,height=2)
label4.pack(padx=20,pady=30)


form.mainloop()