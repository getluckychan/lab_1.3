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

    def read(self):
        self.set_long(input("Введіть кількість гривень: "))
        self.set_byte(input("введіть кількість копійок: "))

    def sub(self, other):
        print(self.to_string() - other)

    def mul_on_float(self):
        print(self.to_string() * 1.5)

    def compere(self, other):
        if self.to_string() > other:
            print("перше значення більше")
        elif self.to_string() < other:
            print("друге число більше")
        else:
            print("вони рівні")