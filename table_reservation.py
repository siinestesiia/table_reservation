def add_to_dictionary(time_of_day, name, amount, time, phone):
    time_of_day['full_name'] = name
    time_of_day['amount'] = amount
    time_of_day['time'] = time
    time_of_day['phone_number'] = phone[:10]

    print('The table reservation named as ' 
          + time_of_day['full_name'].title() + ' for '
          + time_of_day['amount'] + ' people, at '
          + time_of_day['time'] + 'pm. was successfully made.')


def time_limit(horario, time):
    while True:
        if int(horario) > time:
            print(f'\nThe time must be either {time}pm. or before that.')
            horario = input(f'Enter the time (until {time}pm.): ')
            continue
        else:
            pass    
        break


print('\t-welcome to the table reservation system-\n'.upper())
lunch_dinner = 'Would you like to reserve a table for lunch or dinner?\n'
lunch_dinner += 'Please enter either "lunch" or "dinner": '
reservation_time = input(lunch_dinner).lower()


while True:
    if reservation_time.lower() == 'lunch':
        lunch = {}
        nombre = input('Enter your full name: ')
        cantidad = input('How many of you are coming? ')
        horario = input('Enter the time you\'re coming (until 1pm): ')
        time_limit(horario, 1)
        telefono = input('Enter your phone number: ')
        add_to_dictionary(lunch, nombre, cantidad, horario, telefono)
    elif reservation_time.lower() == 'dinner':
        dinner = {}
        nombre = input('Enter your full name: ')
        cantidad = input('How many of you are coming? ')
        horario = input('Enter the time you\'re coming(until 9pm): ')
        time_limit(horario, 9)
        telefono = input('Enter your phone number: ')
        add_to_dictionary(dinner, nombre, cantidad, horario, telefono)
    else:
        reservation_time = input('You must enter either "lunch" or "dinner": ')
        continue
    break

