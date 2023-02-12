import googletrans
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

#translator
def change(text='type', src='English' , dest='Kannada'):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest =dest1)
    return trans1.text


#function for get data
def data():
    s = combo_sor.get()
    d = combo_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text = masg, src = s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)


#title 
root = Tk()
root.title('Translator')
root.geometry('500x700')
root.config(bg ='light blue')

#titlebox heading
lab_text = Label(root, text='Translator', font=('Times new roman', 40, 'bold'))
lab_text.place(x=500, y=30, height=45, width=300)

#fro frame
frame = Frame(root).pack(side=BOTTOM)

#sourcebox heading
lab_text = Label(root, text='Source Text', font=('Times new roman', 20, 'bold'), fg='white', bg='black')
lab_text.place(x=120, y=120, height=30, width=300)


# source textbox
sor_txt = Text(frame, font=('Times new roman', 15, 'bold'), wrap=WORD)
sor_txt.place(x=70, y=200, height=200, width=480)

#combobox
list_text = list(LANGUAGES.values())

combo_sor = ttk.Combobox(frame, value = list_text)
combo_sor.place(x=70, y=170, height =30, width =100)
combo_sor.set('English')

#for translate button code
Button_change = Button(frame, text='Translate', font=('bold',15),relief = RAISED, command=data, bg='light grey', fg="black")
Button_change.place(x=600, y=280, height=40, width=100)

combo_dest = ttk.Combobox(frame, value = list_text)
combo_dest.place(x=770, y=170, height =30, width =100)
combo_dest.set('Kannada')


# destination box heading

lab_text = Label(root, text=' destination text', font=('Times new roman', 20, 'bold'), fg='white', bg='black')
lab_text.place(x=800, y=120, height=30, width=300)

# destination textbox
dest_txt = Text(frame, font=('Times new roman', 15, 'bold'), wrap=WORD)
dest_txt.place(x=770, y=200, height=200, width=480)

root.mainloop()