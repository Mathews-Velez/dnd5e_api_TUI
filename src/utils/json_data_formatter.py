def format_data(data, data_category):
    #call seperate methods to format the data in the formate appropriate to the data category

    def monster_data(data):
        print("Printing monster data ......")
        #if a list is being printed
        for i in data['results']:
            print(i['index'])

    data_formatters = {'monsters': monster_data(data)}

    data_formatters[data_category]