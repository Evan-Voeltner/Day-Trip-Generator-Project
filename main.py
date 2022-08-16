import random

list_of_destinations = ['Milwaukee', 'West Allis', 'Wisconsin Dells', 'Chicago', ]
list_of_transportations = ['Bus', 'Airplane', 'Rental Car', 'Boat', 'Train', 'Blimp']
list_of_restraunts = []
list_of_entertainment = []
final_trip = {
    'location': '',
    'transportation' : '',
    'restraunt': '',
    'entertainment': ''
}


def select_random(given_list):
    selected_item = random.sample(given_list, k=1)
    return(selected_item.pop())



def confirm_selection():
    location_selection = ''
    transportation_selection = ''
    restraunt_selection = ''
    entertainment_selection = ''

    

    
    print('We will plan your trip for you!')



# print(select_random(list_of_destinations))