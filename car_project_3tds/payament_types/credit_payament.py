import config
from payament_times import *
from car_project_3tds.payament_times.m12 import m12
from car_project_3tds.payament_times.m3 import m3
from car_project_3tds.payament_times.m6 import m6
from car_project_3tds.payament_times.m9 import m9
from car_project_3tds.payament_times.in_time import in_time


def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif (time_option == 2):
        return (m3(desired_car))
    elif (time_option == 3):
        return (m6(desired_car))
    elif (time_option == 4):
        return (m9(desired_car))
    elif (time_option == 5):
        return (m12(desired_car))
    else:
        return'Pagamento invalido.'

