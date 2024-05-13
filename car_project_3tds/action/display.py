from config import *

def display_available_cars():
    formatted_cars = []
    for key, value in available_cars.items():
        formatted_cars.append(f'Carro: {key}, preço: {value}')
    cars_str = '\n'.join(formatted_cars)
    return cars_str

def display_cars_sold():
    formatted_cars = []
    for key, value in cars_sold.items():
        formatted_cars.append(f'carro vendido: {key}, Valor da Venda: {value}')
    cars_str = '\n'.join(formatted_cars)
    return cars_str