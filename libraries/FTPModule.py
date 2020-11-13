import ftplib
from io import BytesIO, StringIO

class FTPConn:
    """
    This class pretends to be used as a context manager 
    providing the connection to an ftp host
    Parameters:
    --------------
    :param ftp_url: host to the ftp connection
    :type ftp_url: str
    :param ftp_user: user to the ftp connection
    :type ftp_user: str
    :param ftp_pass: password to the ftp connection
    :type ftp_pass: str
    :param encoding: ecoding type for the data transfers (i.e utf-8, ascii)
    :type encoding: str
    """
    def __init__(self, ftp_url, ftp_user, ftp_pass, encoding):
        self.ftp = ftplib.FTP(ftp_url, ftp_user, ftp_pass)
        self.ftp.encoding = encoding
    def __enter__(self):
        return self.ftp
    def __exit__(self, ext_type, exc_value, traceback):
        self.ftp.quit()

class FtpM:
    """
    Class to perform ftp operations

    :param ftp_url: host to the ftp connection
    :type ftp_url: str
    :param ftp_user: user to the ftp connection
    :type ftp_user: str
    :param ftp_pass: password to the ftp connection
    :type ftp_pass: str
    """
    def __init__(self, ftp_url, ftp_user, ftp_pass, ftp_path="/"):
        self.ftp_url = ftp_url
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.encoding = "utf-8"
        self.ftp_path = ftp_path

    def write_str_file(self, string, file_name):
        """
        Method that allows to write a string variable into a file on the ftp host

        :param string: content of the file to be saved
        :type string: str
        :param file_name: destiny filename on the ftp path
        :type file_name: str

        :return: response
        :rtype: str
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            ftp.cwd(self.ftp_path)
            bytes_string = BytesIO(bytes(string, encoding=self.encoding))
            result = ftp.storbinary(f"STOR {file_name}", bytes_string)
            bytes_string.close()
            return result
        
    def write_pandas_csv(self, dataframe, file_name):
        """
        Method that allows to write a pandas DataFrame into a ftp path

        :param dataframe: data to write
        :type dataframe: pandas DataFrame
        :param file_name: name stored in the ftp path
        :type file_name: str

        :return: result of the transfer
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            buffer = StringIO()
            dataframe.to_csv(buffer)
            text = buffer.getvalue()
            bio = BytesIO(str.encode(text))
            result = ftp.storbinary(f"STOR {file_name}", bio)

        return result

    def upload_file(self, local_path, file_name):
        """
        Method that allows to load a local file into a file on the ftp host
 
        :param local_path: location of the local file to upload
        :type local_path: str
        :param file_name: name of the destiny file on the ftp path
        :type file_name: str

        :return: response
        :rtype: str
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            ftp.cwd(self.ftp_path)
            with open(local_path, "rb") as file:
                return ftp.storbinary(f"STOR {file_name}", file)

    def read_file(self, file_name):
        """
        Method that allows to read a file returning the content

        :param file_name: name of the file to be readed
        :type file_name: str

        :return: ftp response in the first position and the value of the file in the second
        :rtype: str, str
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            ftp.cwd(self.ftp_path)
            r = BytesIO()
            ftp_response = ftp.retrbinary(f"RETR {file_name}", r.write)
            value = str(r.getvalue(), encoding=self.encoding)
            r.close()
            return ftp_response, value

    def download_file(self, local_path, file_name):
        """
        Method that allows to download a remote ftp file into a local one
   
        :param local_path: local path to be downloaded the file
        :type local_path: str 
        :param file_name: the name of the file located in the ftp path
        :type file_name: str

        :return: response
        :rtype: str
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            ftp.cwd(self.ftp_path)
            with open(local_path, "w") as file:            
                return ftp.retrlines(f"RETR {file_name}", file.write)

    def ls(self, file_path="/"):
        """
        Method that allows to check the content of a remote ftp path

        :param file_path: the ftp path to scan
        :type file_path: str
        
        :return: content of the path
        :rtype: list
        """
        with FTPConn(self.ftp_url, self.ftp_user, self.ftp_pass, self.encoding) as ftp:
            return ftp.dir(file_path)

