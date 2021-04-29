data = [{
          "id": 1,
          "first_name": "Townsend",
          "last_name": "Dansken",
          "email": "tdansken0@yahoo.com",
          "subscribed": True
        }, {
          "id": 2,
          "first_name": "Mariejeanne",
          "last_name": "Edgar",
          "email": "medgar1@google.es",
          "subscribed": False
        }, {
          "id": 3,
          "first_name": "Sheila",
          "last_name": "McBeith",
          "email": "smcbeith2@bluehost.com",
          "subscribed": False
        }, {
          "id": 4,
          "first_name": "Duncan",
          "last_name": "Kull",
          "email": "dkull3@blinklist.com",
          "subscribed": True
        }, {
          "id": 5,
          "first_name": "Rodger",
          "last_name": "Lockhart",
          "email": "rlockhart4@about.com",
          "subscribed": False
        }]

# Start your code below this line.
# To show how many people (number of people) are subscribed
subscribers = []
for x in data:
    if x["subscribed"] is True:
        subscribers.append(x["first_name"])
print("There are", len(subscribers), "people subscribed.\n")

# To show the names of people who are not subscribed
print("This is a list of people who are not subscribed:")
for i in data:
    if i["subscribed"] is False:
        print(i["first_name"], i["last_name"])

# To show the emails of the people who have not subscribed
print("\nSending special promotion to the following emails:")
for i in data:
    if i["subscribed"] is False:
        print(i["email"])
