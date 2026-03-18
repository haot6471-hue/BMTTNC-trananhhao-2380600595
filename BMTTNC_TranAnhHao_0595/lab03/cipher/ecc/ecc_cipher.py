import ecdsa
import os

# Tạo thư mục lưu trữ khóa nếu chưa tồn tại
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo khóa riêng tư (Signing Key)
        sk = ecdsa.SigningKey.generate() 
        # Lấy khóa công khai (Verifying Key) từ khóa riêng tư
        vk = sk.get_verifying_key()

        # Lưu khóa riêng tư xuống file .pem
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Lưu khóa công khai xuống file .pem
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())
            
        print("Keys generated and saved successfully.")

    def load_keys(self):
        # Tải khóa riêng tư từ file
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Tải khóa công khai từ file
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        # Chuyển message sang định dạng ascii trước khi ký
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key=None):
        # Nếu không truyền key vào, hàm sẽ tự load từ file
        if key is None:
            _, vk = self.load_keys()
        else:
            vk = key
            
        try:
            # Xác thực chữ ký với nội dung gốc
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            # Trả về False nếu chữ ký không khớp hoặc bị chỉnh sửa
            return False

# --- Ví dụ cách sử dụng (Bạn có thể bỏ phần này khi tích hợp vào GUI) ---
if __name__ == "__main__":
    ecc = ECCCipher()
    ecc.generate_keys()
    
    sk, vk = ecc.load_keys()
    msg = "Hello ECC Security"
    
    # Ký
    sig = ecc.sign(msg, sk)
    print(f"Signature: {sig.hex()}")
    
    # Xác thực
    is_valid = ecc.verify(msg, sig, vk)
    print(f"Is valid: {is_valid}")