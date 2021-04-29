# Catherine Sheng
# In the first 20 top posts in a subreddit, count how many awards each post has
# and connect them to the title of their post, then export it to a Excel doc.
# Ordered from most awards to least amount of awards

import requests
import csv


def reddit_extract():
    '''Returns useful data about Reddit posts from a given subreddit.'''
    # Allow user to input a subreddit, default to r/worldnews if empty
    subreddit = input("Enter the subreddit (Ex: r/cats)\n")
    if subreddit == "":
        subreddit = "r/worldnews"

    # Set the necessary header information
    url = f'https://www.reddit.com/{subreddit}/top/.json'
    head = {'user-agent': "Catherine Sheng subreddit Award Sorter"}
    rawdata = requests.get(url, headers=head).json()

    # Return the items of interest.
    return rawdata['data']


def reddit_transform(mydata):
    '''Takes raw data from reddit extraction and returns a dictionary.'''
    # Take the title of 20 top posts and put it into a list
    titleList = []
    title_counter = 0
    for title_counter in range(20):
        titleList.append(mydata['children'][title_counter]['data']['title'])
        title_counter = title_counter + 1

    # For each post, find the total amount of awards it has
    awardList = []
    award_counter = 0
    for award_counter in range(20):
        awardList.append(
            mydata['children'][award_counter]['data']['total_awards_received'])
        award_counter = award_counter + 1

    # Connects the titles to the number of awards it got, in a dictionary
    finDict = {titleList[i]: awardList[i] for i in range(len(titleList))}

    # Organize the dictionary from the most awards to the least amount
    sortValues = sorted(finDict.values(), reverse=True)
    sortDict = {}
    for value in sortValues:
        for key in finDict.keys():
            if finDict[key] == value:
                sortDict[key] = finDict[key]
    return sortDict


def reddit_load_to_csv(sortDict):
    '''Writes spreadsheet-style data to a CSV based on the data object produced
    by the transform function.'''
    header = ['Post_Titles', 'Number_Of_Awards']
    # encoding is set to UTF-8 because it converts unknown characters into text
    with open("Subreddit_Awards.csv", "w", encoding="utf-8") as outputfile:
        writer = csv.writer(outputfile)
        # Sorts Excel file- keys in first column and values in second column
        writer.writerow(header)
        for sort in sortDict:
            writer.writerow([sort, sortDict[sort]])

reddit_load_to_csv(reddit_transform(reddit_extract()))
