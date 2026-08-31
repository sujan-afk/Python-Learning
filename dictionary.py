details = {"name": "Sujan Rajbanshi", "Age": 18, "country" : "Nepal"}

#To copy the dictionary
detail_copy = details.copy()
#Or detail_copy = dict(details)

detail_copy["email"] = "xi.sujan13@gmail.com"
print(detail_copy)

family = [
    {"name": "Sujan Rajbanshi", "Age": 18, "country" : "Nepal"},
    {"name": "Sudip Rajbanshi", "Age": 21, "country" : "South Korea"},
    {"name": "Sabitra Rajbanshi", "Age": 46, "country" : "Nepal"},
    {"name": "Chakai Rajbanshi", "Age": None, "country" : "Saudi Arabia"},
]

for pariwar in family:
    print(pariwar["name"], pariwar["Age"], pariwar["country"], sep=",")