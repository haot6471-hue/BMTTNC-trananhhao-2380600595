from cipher.caesar import ALPHABET
class CaesarCipher:
    def __init__(self) -> None:
        self.alphabet = ALPHABET
    
    def encrypt_text(seft, text : str , key : int ) ->str:
        alphabet_len = len(seft.alphabet)
        text = text.upper()
        encrypted_text =[]
        for letter in text:
            letter_index = seft.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = seft.alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    def decrypt_text(seft, text : str , key : int ) ->str:
        alphabet_len = len(seft.alphabet)
        text = text.upper()
        decrypted_text =[]
        for letter in text:
            letter_index = seft.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = seft.alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)