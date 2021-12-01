from main import Money


def read():
    long = input("Введіть першу кількість гривень: ")
    byte = input("введіть першу кількість копійок: ")
    money = Money()
    money.set_long(long)
    money.set_byte(byte)
    long1 = input("Введіть  другу кількість гривень: ")
    byte1 = input("введіть другу кількість копійок: ")
    money1 = Money()
    money1.set_long(long1)
    money1.set_byte(byte1)
    long2 = input("Введіть  третю кількість гривень: ")
    byte2 = input("введіть третю кількість копійок: ")
    money2 = Money()
    money2.set_long(long2)
    money2.set_byte(byte2)
    long3 = input("Введіть  третю кількість гривень: ")
    byte3 = input("введіть третю кількість копійок: ")
    money3 = Money()
    money3.set_long(long3)
    money3.set_byte(byte3)
    float_number = float(input("Введіть дробове число"))
    return [money.to_string(), money1.to_string(), money2.to_string(), money3.to_string(), float_number]


def main_func():
    get_read = read()
    first_sum = get_read[0] + get_read[1]
    second_sum = get_read[2] + get_read[3]
    sub_of_sum = first_sum - second_sum
    print("Різниця сум: ", sub_of_sum)
    mul_on_float = get_read[0] * get_read[4]
    print("Множення першого значення на дріб:", mul_on_float)
    if first_sum > second_sum:
        print("Перша сума більша")
    elif first_sum < second_sum:
        print("Друга сума більша")
    else:
        print("Суми однакові")

def display():
    main_func()

display()