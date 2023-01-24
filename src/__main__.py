from api_req_handler import api_req
from json_data_formatter import format_data

def main():
    # display initial welcome message
    print("Welcome, please select below which category you would like more information on.")
    # show initial menu options
    # send the useer to the menu related to their option

    # data = api_req_handler.api_req("ability-scores")
    # print(data)

    #first menu for selecting the first layer of endpoints
    endpoints = ["monsters", "spells"]

    endpoint = endpoints[int(show_menu(endpoints))]

    data = api_req(endpoint)

    format_data(data, endpoint)
    
def show_menu(options):
       for i in range(len(options)):
           print(f"{i} --- {options[i]}")
       return input("Endpoint: ")
def monster_menu():
   print()
main()