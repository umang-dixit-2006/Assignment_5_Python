Dict = {"Umang":98, "Abhinav": 89, "Yash": 90, "Mike": 67, "Akash": 78}

find = input("Enter the student's name: ")

if find in Dict:
    print(f"{find}'s marks: {Dict.get(find)}")
else:
    print("Student not found")
