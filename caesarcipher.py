import string

#Swedish characters added - Å Ä L
ALPHABET = 'abcdefghijklmnopqrstuvwxyzåäö'

SPECIAL_CHARS = string.punctuation
NUMBER_CHARS = string.digits

class Caesar():
    def __init__(self):
        self.string_input = ''
        self.string_encode = ''
        self.string_decode = ''
        self.number_shifts = 0
        choice = 0

        choice = input('Press 1 for encode or 2 for decode: ')
        
        if choice == '1':
            self.encode_message()
        elif choice == '2':
            self.decode_message()
        else:
            print('Please enter 1 for encoding or 2 for decoding')
            self.__init__()


    def review_input(self, input_string):
        for char in input_string:
            if char in SPECIAL_CHARS:
                return False
            elif char in NUMBER_CHARS:
                return False
        return True   
        

    def encode_message(self):
        self.string_input = input('Enter the text you want to encode: ')
        
        if self.review_input(self.string_input) == True:
            self.string_input = self.string_input.lower()
            self.number_shifts = input('How many letters should it shift?: ')
            if self.number_shifts.isnumeric():
                self.number_shifts = int(self.number_shifts)
        else:
            print('Enter characters only please')
            self.encode_message()
        if not self.number_shifts in range(1, 29):
            print('\n=== Please enter a number between 1-28 ===\n\n\n')
            self.encode_message()
        else:
            self.encode_string(self.string_input, self.number_shifts)
        
        
    def encode_string(self, tempstring, tempshifts):
        for letter in tempstring:
            if letter.isspace():
                self.string_encode += " "
            else:
                
                index_orig = ALPHABET.index(letter)
                shift = tempshifts + index_orig
                if shift >= len(ALPHABET):
                    shift = (shift - len(ALPHABET))
                
                self.string_encode += ALPHABET[(shift)]

        print(self.string_encode + "\n\n")
        self.__init__()



    def decode_message(self):
        self.string_input = input('Enter the text you want to decode: ')
        
        if self.review_input(self.string_input) == True:
            self.decode_string(self.string_input)
        else:
            print('Enter characters only please.')
            self.decode_message()
        
        
    def decode_string(self, tempstring):

        for x in range(len(ALPHABET)):
            self.string_decode = ""
            for letter in tempstring:
                if letter.isspace():
                    self.string_decode += " "
                else:
                    index_orig = ALPHABET.index(letter)
                    shift = index_orig - x
                    if shift < 0:
                        shift = (shift + len(ALPHABET))                    
                    self.string_decode += ALPHABET[(shift)]
                    
            print("SHIFT VALUE: " + str(x) + "\t\t" + self.string_decode)
        self.__init__()
                    
                    
cc = Caesar()
        
