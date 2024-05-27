from abc import ABC, abstractmethod

class Cipher(ABC):
    def __init__(self):
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    @property
    def alphabet(self):
        return self._alphabet
    
    def encrypt_message(self, message):
        encrypted_message = ""
        message = message.upper()
        for char in message:
            if char in self._alphabet:
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_message(self, message):
        decrypted_message = ""
        message = message.upper()
        for char in message:
            if char in self._alphabet:
                decrypted_message += self._decrypt_letter(char)
            else:
                decrypted_message += char
        return decrypted_message

    @abstractmethod
    def _encrypt_letter(self, letter):
        pass

    @abstractmethod
    def _decrypt_letter(self, letter):
        pass
