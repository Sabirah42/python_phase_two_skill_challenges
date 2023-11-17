class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]


    def remove_vowels_solved(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
                #("aeiou")  0 -> self.text[:0] ("")  + self.text[0+1(1):] ("eiou") = "eiou"
                #("eiou")   0 -> self.text[:0] ("")  + self.text[0+1(1):] ("iou")  = "iou"
                #("iou")    0 -> self.text[:0] ("")  + self.text[0+1(1):] ("ou")   = "ou"
                #("ou")     0 -> self.text[:0] ("")  + self.text[0+1(1):] ("o")    = "o"
                #("o")      0 -> self.text[:0] ("")  + self.text[0+1(1):] ("")     = ""
            else:
                i += 1
        return self.text
    
    def remove_vowels_original(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
                #("aeiou")   0 -> self.text[:0] ("")    +  self.text[0+1(1):] ("eiou") = "eiou"
                #("eiou")    1 -> self.text[:1] ("e")   +  self.text[1+1(2):] ("ou")   = "eou"
                #("eou")     2 -> self.text[:2] ("eo")  +  self.text[2+1(3):] ("")     = "eo"
            
            i += 1
        return self.text

remover = VowelRemover("aeiou")
print(remover.remove_vowels_original())