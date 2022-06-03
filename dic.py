
# Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary

from email.headerregistry import Address
from unittest import skip


student = {}
print(student)

student['first_name'] = "Mundu"
student['last_name'] = "joana"
student['gender'] = "female"
student['age'] = 12
student['marital status'] = "married"
student['skills'] = ['html','Css', 'JavaScript','Kotlin']
student['country'] = "Kenya"
student['city'] = "Kampala"
student["address"] = {
    'street':'karen,Rd',
    'zipcode':'00100'
}

print(student)
address_place = student['address']='korongo'
print((address_place))