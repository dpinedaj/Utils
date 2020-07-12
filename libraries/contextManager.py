
#The manual definition of a context manager
class context_manager:
    def __init__(self, creds):
        self.creds = creds
        self.conn = None
        self.cursor = None
    def __enter__(self):
        self.conn = ""
        self.cursor = ""
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()
        self.cursor.close()


creds = {"host":"1.2.3.4.5", "port":1234, "user":"admin", "pwd":"admin"}
with context_manager(creds) as cm:
    values = cm.cursor.query("")


#The contextlib tool
from contextlib import contextmanager

@contextmanager
def conn(creds):
    conn = open("a.txt", "w")
    yield conn
    conn.close()

#Usage:
with conn(creds) as c:
    c.execute()

