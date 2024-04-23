import os
from ErrorHandler import *
from cryptography import * 
from cryptography.fernet import Fernet
class Cryptographer:
        def write_key():
            try:
                key = Fernet.generate_key() 
                with open("key.key", "wb") as key_file: 
                    key_file.write(key) 
            except Exception as err:
                Handler = ErrorHandler()
                Handler.error_print(str(err))
        
        def encrypt(password:str):
            try:
                key = open("key.key", "rb").read()
                f = Fernet(key)
                password = password.encode()
                encrypted_password = f.encrypt(password)
                return encrypted_password.decode()
            except Exception as err:
                Handler = ErrorHandler()
                Handler.error_print(str(err))

        def decrypt(encrypted_password):
            try:
                key = open("key.key", "rb").read() 
                f = Fernet(key)
                decrypted_password = f.decrypt(encrypted_password)
                decoded_decrypted_pass = decrypted_password.decode()
                return decoded_decrypted_pass
            except Exception as err:
                print('an error found !')
                tb = err.__traceback__
                while tb is not None:
                    print({
                        "filename": os.path.split(tb.tb_frame.f_code.co_filename)[1],
                        "method": tb.tb_frame.f_code.co_name,
                        "line": tb.tb_lineno
                    })
                    tb = tb.tb_next
    
