import requests

url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
rawdata = requests.get(url).json()

# look for rows (which is a list of dictionaries) in rawdata
onlyRows = rawdata['rows']

# counter is for the ranks
counter = 1

# take each dictionary in onlyRows and organize them by rank, name and download count
for i in onlyRows:
    print("Rank #:", counter, "\n"
        "Name:", i['project'], "\n"
        "Download Count:", i['download_count'], "\n"
        )
    counter = counter + 1
