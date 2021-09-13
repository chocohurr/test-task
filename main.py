import base64
import ast
import binascii


class NoneException(Exception):
    pass


if __name__ == '__main__':

    try:
        with open("info.txt") as f:
            input_string = f.read()
    except OSError as e:
        print(e)
        exit(1)

    try:
        decoded_bytes: bytes = base64.b64decode(input_string)
        decoded_string: str = decoded_bytes.decode("UTF-8")
    except (binascii.Error, UnicodeError):
        print("Decode error")
        exit(2)

    try:
        cars_and_customers: dict = ast.literal_eval(decoded_string)
    except SyntaxError:
        print("Parse data error")
        exit(3)

    try:
        cars: list = cars_and_customers.get('cars')
        customers: list = cars_and_customers.get('customers')

        for customer in customers:
            balance: int = int(customer.get('balance'))
            for car in cars:
                price: int = int(car.get('price'))
                if balance >= price:
                    brand: str = car.get('brand')
                    model: str = car.get('model')
                    firstname: str = customer.get('firstname')
                    lastname: str = customer.get('lastaname')
                    if (brand is not None and model is not None and
                            firstname is not None and lastname is not None):
                        print(f"Car {brand} {model} can be offered "
                              f"for {firstname} {lastname}")
                    else:
                        raise NoneException
    except (TypeError, ValueError, NoneException):
        print("Invalid data")
        exit(4)
