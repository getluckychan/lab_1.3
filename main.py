class Money:
    def __init__(self):
        self.__long = 1
        self.__byte = 1

    def set_long(self, long):
        self.__long = long

    def set_byte(self, byte):
        self.__byte = byte

    def get_long(self):
        return self.__long

    def get_byte(self):
        return self.__byte

    def to_string(self):
        value = float(str(self.__long) + "." + str(self.__byte))
        return value


get = Money()
get.set_long(11)
get.set_byte(50)
print(get.to_string())
