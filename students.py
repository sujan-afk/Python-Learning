import csv

name = input("What is your name? ")
address = input("What is your address ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": address})