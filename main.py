import base64
import ast
import binascii


if __name__ == '__main__':
    try:
        with open("info.txt") as f:
            input_string = f.read()
        decoded_bytes: bytes = base64.b64decode(input_string)
    except (OSError, binascii.Error) as e:
        print(e)
        exit(1)

    decoded_string: str = decoded_bytes.decode("UTF-8")
    cars_and_customers: dict = ast.literal_eval(decoded_string)

    cars: list = cars_and_customers.get('cars')
    customers: list = cars_and_customers.get('customers')

    for customer in customers:
        balance: int = customer.get('balance')
        for car in cars:
            price: int = car.get('price')
            if balance >= price:
                print(f"Car {car.get('brand')} {car.get('model')} can be "
                      f"offered for {customer.get('firstname')} "
                      f"{customer.get('lastaname')}")
