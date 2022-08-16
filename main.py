import random

list_of_destinations = ['Milwaukee', 'West Allis', 'Wisconsin Dells', 'Chicago', ]
list_of_transportations = ['Bus', 'Airplane', 'Rental Car', 'Boat', 'Train', 'Blimp']
list_of_restraunts = []
list_of_entertainment = []



def select_random(given_list):
    selected_item = random.sample(given_list, k=1)
    return(selected_item.pop())

def does_user_agree(current_key, current_item):
    user_input = input(f'{current_item} has been selected as your {current_key}. Do you like this {current_key}? Enter y/n: ')
    input_is_valid = False
    user_likes_selection = False

    while input_is_valid != True:
        if user_input != 'y' or user_input != 'n':
            print('Your response was invalid, please only type a "y" or "n": ')
            break
        else:
            input_is_valid = True
        
    if user_input == 'y':
        user_likes_selection = True
        
    return user_likes_selection



def create_trip(location_list, transportation_list, restraunt_list, entertainment_list):
    location_selection = select_random(location_list)
    transportation_selection = select_random(transportation_list)
    restraunt_selection = select_random(restraunt_list)
    entertainment_selection = select_random(entertainment_list)
    final_trip = {
    'location': '',
    'transportation' : '',
    'restraunt': '',
    'entertainment': ''
    }  
    trip_confirmed = False

    while trip_confirmed != True:

        if does_user_agree('location', location_selection):
            final_trip.update({"location" : location_selection})
            print(f'{location_selection} has been selected as your location!')

        

    

    
    print('We will plan your trip for you!')



# print(select_random(list_of_destinations))