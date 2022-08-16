import random

list_of_destinations = ['Milwaukee', 'West Allis', 'Wisconsin Dells', 'Chicago', ]
list_of_transportations = ['Bus', 'Airplane', 'Rental Car', 'Boat', 'Train', 'Blimp']
list_of_restraunts = []
list_of_entertainment = []



def select_random(given_list):
    selected_item = random.sample(given_list, k=1)
    return(selected_item.pop())



def does_user_agree(given_response):
    current_response = given_response
    input_is_valid = False
    user_likes_selection = False

    while input_is_valid != True:
        if current_response != 'y' or current_response != 'n':
            given_response = input('Your response was invalid, please only type a "y" or "n": ')
            break
        else:
            input_is_valid = True
        
    if given_response == 'y':
        user_likes_selection = True
        
    return user_likes_selection



def make_selection(current_category, current_category_list):
    current_selection = select_random(current_category_list)
    selection_confirmed = False

    while selection_confirmed != True:
        user_input = input(f'{current_selection} has been selected as your {current_category}. Do you like this {current_category}? Enter y/n: ')

        if does_user_agree(user_input):
            print(f'{current_selection} has been selected as your {current_category}!')
            return({current_category : current_selection})
        else:
            print(f'Sorry, we will find another {current_category}')
            current_selection = select_random(current_category_list)



def create_trip(location_list, transportation_list, restraunt_list, entertainment_list):
    final_trip = {
    'location': '',
    'transportation' : '',
    'restraunt': '',
    'entertainment': ''
    }  
    
    trip_confirmed = False

    print('We will plan your trip for you!')

    while trip_confirmed != True:
        final_trip.update(make_selection('location', location_list))
        final_trip.update(make_selection('transportation', transportation_list))
        final_trip.update(make_selection('restraunt', restraunt_list))
        final_trip.update(make_selection('entertainment', entertainment_list))

        print('Here is the trip we have made for you: ' + final_trip)





            

        

    

    
    