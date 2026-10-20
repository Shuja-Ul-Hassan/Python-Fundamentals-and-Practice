# Hands On Project
# Student Grade Book
def add_students(records): # making function to add student in records
    
    name=input("Enter Students's Name: ")
    roll_num=input("Enter The Roll Number: ") # asking name and rollnumber to add in records
    
    if roll_num in records:
        print("This Student is Already included.")
        return
    marks=[]
    subjects=["English","Urdu","Math"] 
    for subject in subjects: # adding grades according to subjects that are taught
        while True: # while the user enters correct numbers for marks
                enter_marks=int(input(f"Enter {subject} marks (0-100): "))
                if 0<=enter_marks<=100:
                    marks.append(enter_marks)
                    break
                else:
                    print("Marks must between 0 and 100. Enter marks Again!")
    records[roll_num]={"Name": name,"Marks": marks} # finally making a records dictionary where rollnumber is the key and the value is another dictionary with name and marks entered before 
    print("Student Added Successfully! \n")

def view_gradebook(records): # function to see the gradebook of students after the data is entered in previous function
    if not records:
        print("No Students Yet!")
        return print(f"\n {'*'*10} Grade Book {'*'*10}")
    for roll_number,data in records.items():
        avg= sum(data["Marks"])/len(data["Marks"]) # average marks of the student
        grade=(
            "A" if avg>=80 else
            "B" if avg>=70 else
            "C" if avg>=60 else
            "D" if avg>=50 else
            "F"
            )
    print(f"\n{'*'*50}\n")

    print(f"Name: {data["Name"]}")
    print(f"Roll Number: {roll_number}") #output for the function gradebook
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
    print(f"English Marks: {data["Marks"][0]}")
    print(f"Urdu Marks: {data["Marks"][1]}")
    print(f"Math Marks: {data["Marks"][2]}")

    print(f"\n{'*'*50}\n")
def main(): #main function that is used to call all the functions created before by taking user input
    record={}
    print("\nStudents Grade Book")
    while True:
        print("1. Add Student")
        print("2. View Grade Book") 
        print("3. Exit")
        option=input("Choose one of the Options: ")
        if option=="1":
            add_students(record)
        elif option=="2":
            view_gradebook(record)
        elif option=="3":
            print("Thank You!")
            break
        else:
            print("Invalid Option Try Again")
if __name__=="__main__":
    main()
