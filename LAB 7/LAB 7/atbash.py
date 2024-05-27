from cipher import Cipher

class AtbashCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.cipherbet = self.alphabet[::-1]
    
    def _encrypt_letter(self, letter):
        index = self.alphabet.find(letter)
        return self.cipherbet[index]

    def _decrypt_letter(self, letter):
        index = self.cipherbet.find(letter)
        return self.alphabet[index]
