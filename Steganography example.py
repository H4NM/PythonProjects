from PIL import Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os

class Stegowindow():
    def __init__(self):
        self.new_filename = ''
        self.chosen_file = ''
        self.image_formats = ['.jpg', '.jpeg', '.png']
        self.new_image_format = ['.png']
        self.mainwindow = tk.Tk()
        self.mainwindow.title('Steganography Example')
        self.canvas1 = tk.Canvas(self.mainwindow, width = 400, height = 260,  relief = 'raised')
        self.canvas1.pack()
        
        self.main()
        

    def clear_canvas(self):
        self.canvas1.delete("all")

    def select_file(self):
        label3 = tk.Label(self.mainwindow, text='')
        label3.config(font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(250, 40, window=label3)
        
        openedfile = askopenfilename() # show an "Open" dialog box and return the path to the selected
        directory, self.chosen_file = os.path.split(os.path.abspath(openedfile))
        if any(imgformat in self.chosen_file for imgformat in self.image_formats):
            label3['text'] = self.chosen_file
        else:
            self.chosen_file = ''
    
        
    def return_to_menu(self):
        self.clear_canvas()
        self.main()
        
    def window_encode(self):
        self.clear_canvas()
        button3 = tk.Button(text='Select image', command= lambda: self.select_file(), bg='grey', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(60, 40, window=button3)

        self.entry1 = tk.Text(self.mainwindow, height = 9, width = 42)
        self.canvas1.create_window(190, 140, window=self.entry1)

        button4 = tk.Button(text='Encode message', command= lambda: self.encode(), bg='green', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(200, 240, window=button4)

        button7 = tk.Button(text='Go Back', command= lambda: self.return_to_menu(), bg='red', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(100, 240, window=button7)

    
    def window_decode(self):
        self.clear_canvas()
        button5 = tk.Button(text='Select image', command= lambda: self.select_file(), bg='grey', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(60, 40, window=button5)

        self.entry2 = tk.Text(self.mainwindow, height = 9, width = 42)
        self.canvas1.create_window(190, 140, window=self.entry2)


        button6 = tk.Button(text='Decode message', command= lambda: self.decode(), bg='green', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(200, 240, window=button6)

        button7 = tk.Button(text='Go Back', command= lambda: self.return_to_menu(), bg='red', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(100, 240, window=button7)



    def main(self):
        
        
        label1 = tk.Label(self.mainwindow, text='Place a hidden message inside an image')
        label1.config(font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(200, 20, window=label1)

        button1 = tk.Button(text='Encode image', command= lambda: self.window_encode(), bg='green', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(150, 100, window=button1)
        
        button2 = tk.Button(text='Decode image', command= lambda: self.window_decode(), bg='green', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(250, 100, window=button2)

        self.mainwindow.mainloop()

        
    def genData(self, data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):

        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                                                            imdata.__next__()[:3] +
                                                            imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                    if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                            pix[j] -= 1

                    elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                            if(pix[j] != 0):
                                    pix[j] -= 1
                            else:
                                    pix[j] += 1
            
            if (i == lendata - 1):
                    if (pix[-1] % 2 == 0):
                            if(pix[-1] != 0):
                                    pix[-1] -= 1
                            else:
                                    pix[-1] += 1

            else:
                    if (pix[-1] % 2 != 0):
                            pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

                newimg.putpixel((x, y), pixel)
                if (x == w - 1):
                        x = 0
                        y += 1
                else:
                        x += 1

    # Encode data into image
    def encode(self):
        if self.chosen_file == '':
            messagebox.showinfo("No file", "Please select a file to encode.")
            return

        img = self.chosen_file
        image = Image.open(img, 'r')

        data = self.entry1.get("1.0", 'end-1c')
        
        if (len(data) == 0):
            messagebox.showinfo("No text", "Please enter text to encode.")
            return
            

        self.newimg = image.copy()
        self.encode_enc(self.newimg, data)
        self.get_new_filename_window()

    def save_newfile(self, entered_name):
        if any(imgformat in entered_name for imgformat in self.new_image_format):
            new_img_name = entered_name
            try:
                self.newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
                messagebox.showinfo("Success", ("The image saved successfully" ))
            except:
                messagebox.showwarning("Error", "Something went wrong with saving the new file")
        else:
            messagebox.showwarning("Image format", "Please export to .png format")
         

    def get_new_filename_window(self):
        self.secondwindow=tk.Toplevel(self.mainwindow)
        self.secondwindow.title('Enter a new file name')

        self.canvas2 = tk.Canvas(self.secondwindow, width = 300, height = 130,  relief = 'raised')
        self.canvas2.pack()
        
        label4 = tk.Label(self.secondwindow, text='Name of new file (With extension)')
        label4.config(font=('helvetica', 8, 'bold'))
        self.canvas2.create_window(140, 20, window=label4)

        entry2 = tk.Entry(self.secondwindow, text='', width=45)
        self.canvas2.create_window(150, 40, window=entry2)


        button6 = tk.Button(self.secondwindow, text='Create file', command= lambda: self.save_newfile(entry2.get()), bg='green', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas2.create_window(140, 100, window=button6)


    def decode(self):
        
        print(self.chosen_file)
        if self.chosen_file == '':
            messagebox.showinfo("No file", "Please select a file to encode")
            return
        
        img = self.chosen_file
        image = Image.open(img, 'r')

        data = ''
        imgdata = iter(image.getdata())

        while (True):
                pixels = [value for value in imgdata.__next__()[:3] +
                                                                imgdata.__next__()[:3] +
                                                                imgdata.__next__()[:3]]
                binstr = ''

                for i in pixels[:8]:
                        if (i % 2 == 0):
                                binstr += '0'
                        else:
                                binstr += '1'

                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                    self.entry2.delete("1.0", 'end-1c')
                    self.entry2.insert('end-1c', data)
                    return

run = Stegowindow()

