import string
import random
import tkinter as tk
from tkinter import messagebox

LETTERS = string.ascii_letters
NUMBERS = string.digits

#String.punctuation can be used, but as described
#below i chose to exclude it due to inconsistencies
#with which are accepted by some services
#PUNCTUATION = string.punctuation

#Chose only a specific set of special symbols
#since some aren't allowed on some services
#Also duplicated the set to ensure that it is selected by the random method
PUNCTUATION = "@!*&#$^%@!*&#$^%"

main = tk.Tk()
main.title('Secure Password Generator')
generated_pw = ''   

def copy_password():
    main.clipboard_clear()
    main.clipboard_append(entry1.get())
    main.update()


def get_password():
    slider_val = slider.get()
    pass_ctg = ''
    if c_val1.get() != 1 and c_val2.get() != 1 and c_val3.get() != 1:
        messagebox.showinfo("Missing Checkboxes", "Please tick a checkbox")   
    else:
        if c_val1.get() == 1:
            pass_ctg += LETTERS
        if c_val2.get() == 1:
            pass_ctg += NUMBERS
        if c_val3.get() == 1:
            pass_ctg += PUNCTUATION
        
        password = ''.join([random.choice(pass_ctg) for _ in range(slider_val)])
        entry1.delete(0,tk.END)
        entry1.insert(0,password)
        

def window():
    global slider
    global c_val1
    global c_val2
    global c_val3
    global canvas1
    global entry1
    c_val1 = tk.IntVar(value=1)
    c_val2 = tk.IntVar(value=1)
    c_val3 = tk.IntVar(value=1)
    
    canvas1 = tk.Canvas(main, width = 400, height = 260,  relief = 'raised')
    canvas1.pack()

    label1 = tk.Label(main, text='Generate Password')
    label1.config(font=('helvetica', 12, 'bold'))
    canvas1.create_window(200, 20, window=label1) 
    
    slider = tk.Scale(main, from_=6, to=100, orient=tk.HORIZONTAL)
    canvas1.create_window(80, 90, window=slider)
 
    checkbox1 = tk.Checkbutton(main, text='Letters',variable=c_val1, onvalue=1, offvalue=0)
    canvas1.create_window(180, 98, window=checkbox1)

    checkbox2 = tk.Checkbutton(main, text='Number',variable=c_val2, onvalue=1, offvalue=0)
    canvas1.create_window(260, 98, window=checkbox2)
    
    checkbox3 = tk.Checkbutton(main, text='Symbols',variable=c_val3, onvalue=1, offvalue=0)
    canvas1.create_window(340, 98, window=checkbox3)

    entry1 = tk.Entry(main, text='', width=55)
    canvas1.create_window(200, 230, window=entry1)

    
    label2 = tk.Label(main, text='Number of characters:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(85, 65, window=label2)
    

    button1 = tk.Button(text='Generate Password', command= lambda: get_password(), bg='green', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 190, window=button1)

    button2 = tk.Button(text='Copy', command= lambda: copy_password(), bg='red', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(285, 190, window=button2)
    
    main.mainloop()


window()
