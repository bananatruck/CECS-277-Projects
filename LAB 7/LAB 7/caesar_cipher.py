from cipher import Cipher

class CaesarCipher(Cipher):
    def __init__(self, shift):
        super().__init__()
        if 0 <= shift <= 25:
            self.shift = shift
        else:
            raise ValueError("Shift value must be between 0 and 25.")
        self.cipherbet = self.alphabet[self.shift:] + self.alphabet[:self.shift]
    
    def _encrypt_letter(self, letter):
        index = self.alphabet.find(letter)
        return self.cipherbet[index]

    def _decrypt_letter(self, letter):
        index = self.cipherbet.find(letter)
        return self.alphabet[index]
