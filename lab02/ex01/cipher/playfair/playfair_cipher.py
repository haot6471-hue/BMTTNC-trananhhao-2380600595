class PlayFairCipher:

    def create_matrix(self, key):
        key = key.upper().replace("J", "I")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        key_not_repeat = ""
        for letter in key:
            if letter not in key_not_repeat:
                key_not_repeat += letter
        matrix = list(key_not_repeat)
        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c


    def playfair_encrypt(self, plain_text, key):

        matrix = self.create_matrix(key)
        plain_text = plain_text.upper().replace(" ", "").replace("J", "I")
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, key):
        matrix = self.create_matrix(key)
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text