from config import *

def debit_payament(desired_car):
    return f'Pagamento realizado por débito no valor de {available_cars.get(desired_car)}'
