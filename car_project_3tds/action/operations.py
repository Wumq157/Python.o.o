from config import *
from action.display import display_available_cars

def purchase(car, value):
    new_car = car
    car_value = value
    available_cars.update({new_car: car_value })
    print(f'Carro {car} comprado pelo valor {value}')
    return display_available_cars()

def sale(desired_car):
    car_sold = available_cars.pop(desired_car)
    cars_sold[desired_car] = car_sold
    return f'Carro {desired_car} vendido'