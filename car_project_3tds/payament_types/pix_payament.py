from config import *

def pix_payament(desired_car):
    return f'Pagamento realizado por Pix no valor de {available_cars.get(desired_car)}'
