def add_foods(foods):
    sixth_letter = []
    not_foods = []
    short_foods = []
    for food in foods:
        try:
            sixth_letter.append(food[5])
        except TypeError:
            not_foods.append(food)
        except IndexError:
            short_foods.append(food)
        #checks each list to see if the food is or isnt a string
    print(f'Sixth Letters: {sixth_letter}')
    print(f'Short Foods: {short_foods}')
    print(f'Not Foods: {not_foods}')
    print('\n')
#prints the food into seperate lists depending on if they are a string, have 6 letters or dont
#
add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True,'chicken','rice','radish'])