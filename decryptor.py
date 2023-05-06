#!/bin/python3
'''
@date: May 6, 2023
@author: yigitoo
@brief: This file will use for encrypting our docx data.
'''
# Libraries i need.
import os
import base64
import codecs
'''
@brief: Class for encrypt .doc/x files.
'''
class Decryptor:
    file_data: str

    '''
        @brief: Constructor of class.
    '''
    def __init__(self, file_data: str = None):
        self.file_data = file_data

        result = self.decrypt()
        
        if result != True:
            print(f"\nError cannot encrypt this file. ({self.file_path})")
        
    '''
        @brief: This is main decryption function.
    '''
    def decrypt(self) -> bool:
        if type(self.file_data) != str:
            return False
        
        try:
            self.decrypted_data = self.secret_decryptor()

            if self.decrypted_data == None:
                raise NotImplementedError("DECYPTED TEXT IS NONE!!!")

            print(f"Program finished and file decrypted: {os.path.base_name(self.file_path)}\nData:{self.decrypted_data}")
            return True

        except Exception as errors:
            print(f"Errors:\n--------\n{errors}")
            return False
        

    def secret_decryptor(self) -> str | None:
        if type(self.file_data) != str:
            raise TypeError(f"Cannot get string data for [text_data]: type(text_data) = {type(self.file_data)}")
        return self.decode_base64(self.decode_rot13(self.file_data))
    
    def decode_rot13(data: str = None) -> str | None:
        if data is not None:
            result = codecs.decode(data, 'rot_13')
            return result
        return None

    def decode_base64(self, data: str = None) -> str | None:
        if data is not None:
            base64_bytes = data.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            result = message_bytes.decode('utf-8')
            return result
        return None

