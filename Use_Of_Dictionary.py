cricket_scores = {
    "India": 325,
    "Australia": 298,
    "England": 310,
    "Pakistan": 287,
    "South Africa": 301,
    "New Zealand": 276,
    "Sri Lanka": 265,
    "Bangladesh": 242,
    "Afghanistan": 221,
    "West Indies": 289,
    "Zimbabwe": 205,
    "Ireland": 214,
    "Scotland": 192,
    "Netherlands": 183,
    "United Arab Emirates": 176,
    "Oman": 169,
    "Namibia": 158,
    "Canada": 147,
    "United States": 162
}

#create
cricket_scores["Nepal"] = 198
#Read
print(cricket_scores.get("Nepal"))
#Update
cricket_scores["Oman"] = 54
#Delete
del cricket_scores["Canada"]

print(cricket_scores)