# Step A: A List
#names = ["Ava", "Ben", "Cara", "Dev"]
#print(names)

# Step B: A Loop
# names = ["Ava", "Ben", "Cara", "Dev"]
# for person in names:
#    print("Checking", person)

# Step C: A Dictionary
#user = {"name": "Ava Chen", "days_inactive": 120}
#print(user["name"])
#print(user["days_inactive"])

# Step D: A list of Dictionaries
#users = [
#    {"name": "Ava Chen", "days_inactive": 120},
#    {"name": "Ben Ortiz", "days_inactive": 75},
#    {"name": "Cara Singh", "days_inactive": 12},
#    {"name": "Dev Patel", "days_inactive": 200},
#]

#for user in users:
#    print(user["name"], "has been inactive for", user["days_inactive"], "days")

#Step E: A decision inside the loop
#users = [
#    {"name": "Ava Chen", "days_inactive": 120},
#    {"name": "Ben Ortiz", "days_inactive": 75},
#    {"name": "Cara Singh", "days_inactive": 12},
#    {"name": "Dev Patel", "days_inactive": 200},
#]
#for user in users:
#    if user["days_inactive"] > 90:
#        print(user["name"], "is stale")

#Step F: A counter
stale_count = 0
users = [
    {"name": "Ava Chen", "days_inactive": 120},
    {"name": "Ben Ortiz", "days_inactive": 75},
    {"name": "Cara Singh", "days_inactive": 12},
    {"name": "Dev Patel", "days_inactive": 200},
    {"name": "Eve Johnson", "days_inactive": 60},
    {"name": "Frank Smith", "days_inactive": 90},
    {"name": "Grace Lee", "days_inactive": 300},
]
for user in users:
    if user["days_inactive"] > 90:
        print(user["name"], "is stale")
        stale_count = stale_count + 1
print("Total stale accounts:", stale_count)