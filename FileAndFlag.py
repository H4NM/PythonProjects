import string
import re
import os, os.path
import time
import magic
from PIL import Image, ExifTags


IMAGE_FORMATS = ['.jpg', '.JPG', '.png', '.PNG', '.gif', '.GIF']

class File():
    def __init__(self, file, **kwargs):
        
        self.file_name = file
        self.temp_open = open(self.file_name, "rb").read()
        self.temp_decoded = self.temp_open.decode('ISO-8859-1')
        self.string_list = string_list = re.findall("[a-zA-Z0-9]+", self.temp_decoded)

        self.found_keywords = {}


        self.file_stats()

        if self.check_keyw_strings():
            print("\n=====================================")
            print("!! Matching keyword strings found! !!")
            print("=====================================")
            self.collection_keyword()
        else:
            print('No matching keyword string found')
            
        self.check_file_img()
        
    def print_strings(self):
        for string in self.string_list:
            print(string + "\n")

    def check_keyw_strings(self):
        string_counter = 0
        
        for string in self.string_list:
            string_counter += 1
            if string in KEYWORDS:
                if string in self.found_keywords:
                    self.found_keywords[(string + " " + str(len(self.found_keywords)))] = (string_counter)
                else:
                    self.found_keywords[string] = (string_counter)
        if len(self.found_keywords) == 0:
           return False 
        else:
           return True

    def file_stats(self):
        print('================ FILE DETAILS =================') 
        print('Modified time     :', time.ctime(os.path.getmtime(self.file_name)))
        print('Perm change time  :', time.ctime(os.path.getctime(self.file_name)))
        print('Bytes             :', os.path.getsize(self.file_name))
        print('Number of strings :', len(self.string_list))
        print('File              :', self.get_header())
        print('===============================================')

    def collection_keyword(self):
        if isinstance(self.found_keywords, dict):
            for k, v in self.found_keywords.items():
                if hasattr(v, '__iter__'):
                    print(k)
                    dumpclean(v)
                else:
                    print('%s : %s' % (k, v))

    def get_header(self):
        f = magic.Magic(uncompress=True)
        val = f.from_file(self.file_name)
        return val

    def get_type(self):
        f = magic.Magic(mime=True, uncompress=True)
        val = f.from_file(self.file_name)
        return val

    def check_file_img(self):
        for frmt in IMAGE_FORMATS:
            if frmt in self.file_name:
                self.choice_exif_data()
                self.decode_stego()
                

    def decode_stego(self):
        try:
            image = Image.open(self.file_name, 'r')
         
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
                    print("============== STEGOGRAPHY DATA ===============")
                    return print(data)
        except:
            print('Unable to check for hidden message.')
                
    def choice_exif_data(self):
        img = Image.open(self.file_name)

        img_exif = img.getexif()
        if img_exif:
            print("================== EXIF DATA ==================")
            img_exif_dict = dict(img_exif)
            for key, val in img_exif_dict.items():
                if key in ExifTags.TAGS:
                    print(ExifTags.TAGS[key] + " - " + str(val))
        else:
            print("Sorry, there doesn't seem to be any exif-data.")

####### 
FILENAME = "222.jpg"
KEYWORDS = ['flag', 'htb', 'ctf', 'FLAG', 'HTB', 'CTF', '{', '}']

f = File(FILENAME)


