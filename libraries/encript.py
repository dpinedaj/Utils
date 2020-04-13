#!/usr/bin/python

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

#Local Libraries
from . import files as fl
from .constants import Constants as Cts
from .struct import Struct
from .utils import Utils


class Encript:
    def __init__(self, ar_key, ar_logs=None):
        self.cts = Cts()
        self.key = hashlib.sha256(ar_key.encode()).digest()
        self.logs = ar_logs
        self.msg = Struct(
            **fl.get_properties_section(self.cts.GLOBALCONFIG,
                                             self.cts.SECCIONENCRIPT)
        )
        self.msg_info = self.msg.text_info
        self.msg_error = self.msg.text_error

    def __pack(self, ar_text_en):

        blockSize = AES.block_size
        return ar_text_en + (blockSize\
                            - len(ar_text_en) % blockSize)\
                            * chr(blockSize - len(ar_text_en) % blockSize)

    def __unpack(self, ar_text_des):

        return ar_text_des[:-ord(ar_text_des[len(ar_text_des)-1:])]


    def encrypt_text(self, ar_text):

        text = None
        vector = None
        code = None
        encrypted = None
        exitValue = None

        try:
            text = self.__pack(ar_text)
            vector = Random.new().read(AES.block_size)
            code = AES.new(self.key, AES.MODE_CBC, vector)
            encrypted = base64.b64encode(vector + code.encrypt(text.encode()))

            exitValue = self.cts.OK
            if self.logs is not None:
                self.logs.info(self.msg.text_info)

        except Exception as exc:
            print(str(exc))
            encrypted = None
            exitValue = self.cts.ERROR
            if self.logs is not None:
                self.logs.error(self.msg.text_error)

        return encrypted, exitValue


    def decrypt_text(self, ar_text_enc):

        encrypted = None
        vector = None
        code = None
        decrypted = None
        exitValue = None
        try:
            encrypted = base64.b64decode(ar_text_enc)
            vector = encrypted[:AES.block_size]
            code = AES.new(self.key, AES.MODE_CBC, vector)
            decrypted = self.__unpack(code.decrypt(encrypted[AES.block_size:]))\
                .decode(self.cts.DECODE)

            exitValue = self.cts.OK
            if self.logs is not None:
                self.logs.info(self.msg.text_info)

        except Exception as exc:
            print(str(exc))
            decrypted = None
            exitValue = self.cts.ERROR
            if self.logs is not None:
                self.logs.error(self.msg.text_error)

        return decrypted, exitValue


    def encrypt_file(self, ar_file, ar_encrypted_name,
                            ar_file_extension="encrypted"):



        content = None
        vector = None
        code = None
        encryptedContent = None
        try:
            content = fl.full_read(ar_file)
            content = self.__pack(content)
            vector = Random.new().read(AES.block_size)
            code = AES.new(self.key, AES.MODE_CBC, vector)
            encryptedContent = base64.b64encode(vector + code.encrypt(content.encode()))

            fl.write_binary("""{}.{}""".format(ar_encrypted_name,ar_file_extension),
                                     encryptedContent)

            if self.logs is not None:
                self.logs.info(self.msg.encrypt_info.format(ar_file))

            exitValue = self.cts.OK

        except Exception as exc:
            print(str(exc))
            exitValue = self.cts.ERROR
            if self.logs is not None:
                self.logs.error(self.msg.encrypt_error.format(ar_file))

        return exitValue


    def decrypt_file(self, ar_encrypted_file, ar_decrypted_name,
                                ar_file_extension="decrypted"):

        content = None
        vector = None
        code = None
        decryptContent = None
        exitValue = None
        try:
            content = fl.full_read_binary(ar_encrypted_file)
            content = base64.b64decode(content)
            vector = content[:AES.block_size]
            code = AES.new(self.key, AES.MODE_CBC, vector)
            decryptContent = self.__unpack(code.decrypt(content[AES.block_size:])).decode('utf-8')

            fl.write("""{}.{}""".format(ar_decrypted_name, ar_file_extension),
                              decryptContent)

            if self.logs is not None:
                self.logs.info(self.msg.decrypt_info.format(ar_encrypted_file))

            exitValue = self.cts.OK

        except Exception as exc:
            print(str(exc))
            exitValue = self.cts.ERROR
            if self.logs is not None:
                self.logs.error(self.msg.decrypt_error.format(ar_encrypted_file))

        return exitValue
