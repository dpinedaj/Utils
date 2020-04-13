
class Struct:
    """
        Update a dictionary to a Struct instance
    """
    def __init__(self, **ar_parameters):
        """
        
        parameters :
            ar_parameters: dictionary

        exit :
            Struct instance with the dictonary content

        """
        self.__dict__.update(ar_parameters)
