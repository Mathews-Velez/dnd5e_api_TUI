from utils.api_req_handler import api_req
from utils.json_data_formatter import format_data

def main():
    # display initial welcome message
    print("Welcome, please select below which category you would like more information on.")
    # show initial menu options
    # send the useer to the menu related to their option

    # data = api_req_handler.api_req("ability-scores")
    # print(data)

    #first menu for selecting the first layer of endpoints
    menus = ["monster_menu", "spell_menu"]

    show_menu()
    
    data = api_req(endpoint)

    format_data(data, endpoint)

def show_menu(options):
       for i in range(len(options)):
           print(f"{i} --- {options[i]}")
       return input("Endpoint: ")
def monster_menu():

    #submenu for monster querying
    #allow user to type the name of the monster they want to search for, offer auto complete
    #display the live count of monster to be queried
    #allow user to either see all the names of the monsters, while the list is being shown, we can prompt the user to continue down the list or imput the number related to the monster
   options =["Search by name", "Filter list by challenge rating"]
   print("Choose one of the following option to query the monsters endpoint:")
   for option in options:
       print(f"{option.index}--- {option}")
   choice = input("Option: ")

def search_by_name():#wait for the user to give their initail input and then activate the auto complete for them
        index=input("Monster's name: ")
main()