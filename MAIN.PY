import json

print("Student Management System:")
print("press 1 to add student")
print("press 2 to view student")
print("press 3 to search student")
print("press 4 to update student")
print("press 5 to delete student")
print("press 6 to exit")


try:
    with open("student_records.json", "r") as file:
        student = json.load(file)
except FileNotFoundError:
    student = []

while(True):
    a = int(input("enter choice: "))
    print("you selected:", a)
    
    if(a == 1):
        x = int(input("enter student Id: "))
        y = input("enter student name: ")
        z = int(input("enter age: "))
        student.append({"Id": x, "Name": y, "age": z})
        
        # Save data after adding
        with open("student_records.json", "w") as file:
            json.dump(student, file, indent=4)
        print("student added successfully")
        
    elif(a == 2):
        if(student == []):
            print("list is empty")
        else:
            print(student)
        print("viewed student successfully")
        
    elif(a == 3):
        m = int(input("enter student id you want to search: "))
        found = False
        for s in student:
            if s["Id"] == m:
                print("Id:", s["Id"])
                print("Name:", s["Name"])
                print("age:", s["age"])
                found = True
                break
        if found == False:
            print("not found")
            
    elif(a == 4):
        m = int(input("enter student id you want to update: "))
        found = False
        for s in student:
            if s["Id"] == m:
                print("current details:")
                print("Id:", s["Id"])
                print("Name:", s["Name"])
                print("age:", s["age"])
                found = True
                new_name = input("enter name which you want to update:")
                new_age = int(input("enter age which you want to update:"))
                s["Name"] = new_name
                s["age"] = new_age
                print("updated details:")
                print("Id:", s["Id"])
                print("Name:", s["Name"])
                print("age:", s["age"])
                
                # Save data after updating
                with open("student_records.json", "w") as file:
                    json.dump(student, file, indent=4)
                print("updated sucessfully")
                break
        if found == False:
            print("Id not found")
            
    elif(a == 5):
        m = int(input("enter student id you want to delete: "))
        found = False
        for s in student:
            if s["Id"] == m:
                student.remove(s)
                
                # Save data after deleting
                with open("student_records.json", "w") as file:
                    json.dump(student, file, indent=4)
                print("student deleted successfully")
                found = True
                break
        if found == False:
            print("Id not found")
            
    elif(a == 6):
        print("exiting...")
        break
    else:
        print("invalid choice")
