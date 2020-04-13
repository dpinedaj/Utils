from functools import wraps

from .constants import Constants as cts
class Utils:

    @staticmethod
    def try_exc(f):
        @wraps(f)
        def new_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as exc:
                print('Error:', str(exc))
        return new_function

    @staticmethod
    def try_exc_none(f):
        @wraps(f)
        def new_function(*args, **kwargs):
            value = None
            try:
                value = f(*args, **kwargs)
            except Exception as exc:
                print('Error:', str(exc))

            return value
        return new_function

    #TODO ON DEVELOP
    @staticmethod
    def try_exc_logs(f):
        @wraps(f)
        def new_function(self, *args, **kwargs):
            value = None
            exit_value = None
            try:
                value = f(self,*args, **kwargs)
                if value != None:
                    exit_value = self.cts.OK
                    if self.logs != None:
                        self.logs.info(self.msg_info)
            except Exception as exc:
                if self.logs != None:
                    self.logs.error(self.msg_error)
                    self.logs.error(str(exc))
                exit_value = self.cts.ERROR

            return value, exit_value
        return new_function
