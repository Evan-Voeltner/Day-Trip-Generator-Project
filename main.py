import random

list_of_locations = ['Milwaukee', 'West Allis', 'Wisconsin Dells', 'Chicago', ]
list_of_transportations = ['Bus', 'Airplane', 'Rental Car', 'Boat', 'Train', 'Blimp']
list_of_restraunts = ['Mcdonalds', 'Wendys', 'In and Out', 'Carabas', 'Olgas Kitchen']
list_of_entertainment = ['see a play', 'take a segway tour', 'explore a museum', 'take a hike', 'go to a party']



def select_random(given_list):
    selected_item = random.sample(given_list, k=1)
    return(selected_item.pop())


def does_user_agree(given_response):
    current_response = given_response
    input_is_valid = False
    user_likes_selection = False

    while input_is_valid != True:
        if current_response != 'y' and current_response != 'n':
            current_response = input('Your response was invalid, please only type a "y" or "n": ')
        else:
            input_is_valid = True
        
    if current_response == 'y':
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
    category_lists = {
    'location': location_list,
    'transportation' : transportation_list,
    'restraunt': restraunt_list,
    'entertainment': entertainment_list
    }
    
    final_trip = {
    'location': '',
    'transportation' : '',
    'restraunt': '',
    'entertainment': ''
    }  
    
    trip_confirmed = False

    print('We will plan your trip for you!')
        
    final_trip.update(make_selection('location', location_list))
    final_trip.update(make_selection('transportation', transportation_list))
    final_trip.update(make_selection('restraunt', restraunt_list))
    final_trip.update(make_selection('entertainment', entertainment_list))

    while trip_confirmed != True:
        
        print('Here is the trip we have made for you: ' + str(final_trip))
        user_response = input('Would you like to confirm your trip? Enter y/n: ')
        
        if does_user_agree(user_response):
            print(f'Your trip has been confirmed! You will go to {final_trip.get("location")} on a {final_trip.get("transportation")}. There, you will {final_trip.get("entertainment")}, and afterwards go and eat at {final_trip.get("restraunt")}.')
            trip_confirmed = True
        else:
            category_to_change = input('''What would you like to change?:
            location
            transportation
            restraunt
            entertainment
            ''')
            
            final_trip.update(make_selection(category_to_change, category_lists.get(category_to_change)))

        
create_trip(list_of_locations, list_of_transportations, list_of_restraunts, list_of_entertainment)


            

        

    

    
    