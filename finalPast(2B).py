student = {
    "111":{"name":"Ahmad","phone":"0162050170"},
    "222":{"name":"Damia","phone":"0162050180"},
    "333":{"name":"Aimi","phone":"0162050190"}
}

ID = input("enter ID: ")

for datakey, datavalue in student.items():
    # if ID == datakey:
        print(datavalue["name"])
        print(datavalue["phone"])


