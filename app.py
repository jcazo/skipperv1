from tkinter import *

ventana=Tk()
ventana.title('Monitoreo de Pingüinos')
ventana.geometry("380x530")
ventana.iconbitmap('../favicon.ico')
ventana.configure(bg="white")

frame1= Frame(ventana,bg="ghost white")
frame1.pack(fill="both",expand=TRUE)

def show():
    if var_temp.get()==1:
        vtemp="T"

    else:
        vtemp=""

    if var_depth.get()==1:
        var_depth1="D"
    else:
        var_depth1=""

    if var_position.get()==1:
        var_position1="P"
    else:
        var_position1=""

    if var_acceleration.get()==1:
        var_acceleration1="A"
    else:
        var_acceleration1=""

    if var_video.get()==1:
        var_video1="V"
    else:
        var_video1=""
    
    print(vdepth1.get())
    print(vdepth2.get())
    archivo = open("parametros.txt","w")
    archivo.write(vtemp + "," + var_depth1 +  "," + var_position1 +"," + var_acceleration1 +"," + var_video1 +"\n")
    archivo.write(vday.get() + "," + vhour1.get() +  "," +vhour2.get() + "," +  vts.get() +  "," +vdepth1.get()+"," + vdepth2.get())
    archivo.close()



canvas = Canvas(frame1, bg="white",width=120,height=100)
canvas.pack()
imagen=PhotoImage(file="icon.png")
imagen=imagen.subsample(7,7)
canvas.create_image(65,50,image=imagen)

titulo = Label(frame1,text="MONITOREO DE PINGUINOS").pack()
titulo = Label(frame1,text=" ").pack()
seccion1 = Label(frame1,text="PARÁMETROS DE MONITOREO").pack()



var_temp = IntVar()
var_depth = IntVar()
var_position = IntVar()
var_acceleration = IntVar()
var_video = IntVar()

frame2=Frame(frame1,bg="white")

c = Checkbutton(frame2,text="Temperature",variable=var_temp,onvalue=1,offvalue=0)
c.deselect() # iniciar deseleccionado al correr 
c.grid(row=0,column=0)

c= Checkbutton(frame2,text="Depth",variable=var_depth,onvalue=1,offvalue=0)
c.deselect()
c.grid(row=1,column=0)

c= Checkbutton(frame2,text="Position",variable=var_position,onvalue=1,offvalue=0)
c.deselect()
c.grid(row=2,column=0)

c= Checkbutton(frame2,text="Acceleration",variable=var_acceleration,onvalue=1,offvalue=0)
c.deselect()
c.grid(row=0,column=1)

c= Checkbutton(frame2,text="Video",variable=var_video,onvalue=1,offvalue=0)
c.deselect()
c.grid(row=1,column=1)

frame2.grid_columnconfigure(0,weight=1)
frame2.pack()


frame3=Frame(frame1,bg="white")
seccion2 = Label(frame3,text=" ").pack()
seccion2 = Label(frame3,text="CONFIGURACIÓN INICIAL").pack()

frame3.pack(fill="x")

frame4=Frame(frame1,bg="ghost white")



label1 = Label(frame4,text="Day:")
label1.grid(row=0,column=0)
vday = Entry(frame4,width=4)
vday.grid(row=0,column=1)

label1 = Label(frame4,text="Hour1:")
label1.grid(row=1,column=0)
vhour1 = Entry(frame4,width=4)
vhour1.grid(row=1,column=1)

label1 = Label(frame4,text="Hour2:")
label1.grid(row=2,column=0)
vhour2 = Entry(frame4,width=4)
vhour2.grid(row=2,column=1)

label1 = Label(frame4,text="Ts:")
label1.grid(row=0,column=3)
vts = Entry(frame4,width=4)
vts.grid(row=0,column=4)

label1 = Label(frame4,text="Depth1:")
label1.grid(row=1,column=3)
vdepth1 = Entry(frame4,width=4)
vdepth1.grid(row=1,column=4)

label1 = Label(frame4,text="Depth2:")
label1.grid(row=2,column=3)
vdepth2 = Entry(frame4,width=4)
vdepth2.grid(row=2,column=4)

frame4.pack()
frame5=Frame(frame1,bg="white")
myButton = Button(frame5, text="ACEPTAR",command=show).pack()

frame5.pack(fill="x")
ventana.mainloop()