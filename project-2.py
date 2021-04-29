# Catherine Sheng
# Allow user to search by keyword through titles and/or tags from 
# the top 200 articles.

import requests
import csv


def nyt_extract():
    '''Returns useful data about New York Times top stories'''
    apikey = "ZIV5KVGKODTkm37VWzEqNPd2YhvmDUFz"

    requestUrl = f"https://api.nytimes.com/svc/topstories/v2/food.json?api-key={apikey}"
    requestHeaders = {
        "Accept": "application/json"
    }

    rawdata = requests.get(requestUrl, headers=requestHeaders).json()

    return (rawdata['results'])


def nyt_transform(mydata):
    '''Takes raw data from reddit extraction and returns a dictionary.'''
    # get all the titles
    title_List = []
    title_counter = 0
    for title_counter in range(20):
        title_List.append(mydata[title_counter]['title'])
        title_counter = title_counter + 1

    # get all the tags 
    tags_List = []
    tags_counter = 0
    for tags_counter in range(20):
        tags_List.append(mydata[tags_counter]['des_facet'])
        tags_counter = tags_counter + 1
    #des_facat are the tags and they are listed as an array
    # the final output is an array of arrays

    # Connects the titles to the tags in a dictionary
    finDict = {title_List[i]: tags_List[i] for i in range(len(title_List))}

    print(final_Dict)


def nyt_load_to_csv(final_Dict):

        '''Ask user which list they want to search through: titles, tags, or tags and titles. 
    Output an Excel sheet of the titles and tags from the keyword.'''

""" 
    userinput = input("Hello! What do you want to do? Please type in a number.")

    if userinput == 1:
        # run function
    elif userinput == 2:
        # run function   
    elif userinput == 3:
        #run function
    else:
        userinput = input("Sorry that is not an option, please respond with a number (i.e. 1, 2, 3)") 
 """

nyt_transform(nyt_extract())
