import requests

def api_req(endpoint): 
    """Uses the provided topic and optional filters to fetch json data from the dnd5eapi

    Args:
        category (String): _description_

    Returns:
        JSON: the JSON objects holding all relavent data from the api
    """
    # base url for making requests
    #from here the appropriate endpoint is addded on to the url
    URL = "https://www.dnd5eapi.co/api/"
    URL += endpoint
    #test to show count of the end point
    
    r = requests.get(url=URL)
    data = r.json()
    return data
