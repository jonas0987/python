dic={
    "name": "sujeet",
    "roll": 22364,
    "subject":"coding",
    "age":'22'
}

print(dic)
print(dic["name"])

#  empty dir:-----

dic={}


# nested directary-----

student={
    "name":'sujeet',
    "roll":64,
    "subject":{
        "phy":97,
        "chem":94,
        "math":99,
    }

}

print(student)
print(student["subject"]["math"])


#  method:--------------


print(student.keys())
student.clear()
print(student)

print(student.values())
print(student.pop("name"))

print(student.items())
print(list(student.items())) 
print(student.get("name"))
print(student["name"])  #this may give error if you write name2

student.update({"weight":47})   
print(student)