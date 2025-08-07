dictionary = {"Alice": 89, "Mark": 78, "Kira": 88, "Nia": 67, "Rohit": 96}
print(dictionary)
name = input("Enter the students's name:")
print(dictionary.get(name,"Student not found."))
    