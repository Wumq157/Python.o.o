from action.display import *
from config import *
from action.operations import *
from payament_types.credit_payament import *
from payament_types.debit_payament import *
from payament_types.pix_payament import *

while True:
    option = input(menu)
    if option == 'C':
        display_available_cars()
        desired_car = input('Qual carro você quer comprar? ')
        option_payament = input(type_payament)
        if option_payament == 'C':
            prazo = input(time_payament)
            print(credit_payament(desired_car, prazo))
            print(sale(desired_car))
            
        elif option_payament == 'D':
            print(debit_payament(desired_car))
            print(sale(desired_car))
            print(display_cars_sold())

        elif option_payament == 'P':
            print(pix_payament(desired_car))
            print(sale(desired_car))
            print(display_cars_sold())

    elif option == 'V':
        car = input('Qual o nome do Carro a ser vendido? ')
        value = float(input('Qual o valor do carro? '))
        print(purchase(car, value))
        
    elif option == 'Q':
        print('Muito Obrigado!')
        break