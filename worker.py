from main import Money


def main_func():
    first_value = Money()
    first_value.read()
    second_value = Money()
    second_value.read()
    first_value.to_string()
    second_value.to_string()
    first_value.sub(second_value.to_string())
    first_value.mul_on_float()
    first_value.compere(second_value.to_string())


main_func()
