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
class Encryptor:
    file_path: str

    '''
        @brief: Constructor of class.
    '''
    def __init__(self, file_path: str = None):
        self.file_path = file_path

        result = self.encrypt()
        
        if result != True:
            print(f"\nError cannot encrypt this file. ({self.file_path})")
        
    '''
        @brief: This is main encryption function.
    '''
    def encrypt(self) -> bool:
        if type(self.file_path) != str:
            return False
        
        try:
            parsed_docx = self.parse_docx()
            encrypted_data = self.secret_encryptor(parsed_docx)
            self.encrypted_data = encrypted_data
            self.save_it()
            print(f"Program finished and file encrypted: {os.path.base_name(self.file_path)}")
            return True

        except Exception as errors:
            print(f"Errors:\n--------\n{errors}")
            return False

    def parse_docx(self):
        pass

    def secret_encryptor(self, text_data: str = None) -> str:
        if type(text_data) != str:
            raise TypeError(f"Cannot get string data for [text_data]: type(text_data) = {type(text_data)}")
        return self.encode_rot13(self.encode_base64(self.text_data))

    def encode_rot13(data: str = None) -> str | None:
        if data is not None:
            result = codecs.decode(data, 'rot_13')
            return result
        return None

    def encode_base64(self, data: str = None) -> str | None:
        if data is not None:
            message_bytes = data.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            result = base64_bytes.decode('ascii')
            return result
        return None