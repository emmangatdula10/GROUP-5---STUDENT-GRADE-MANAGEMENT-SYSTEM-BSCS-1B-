import json
import os

FILE_NAME = "../Data_Files/student_record.json"
def load_Records():
    if not os.path.exists(FILE_NAME):
        return{}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_Records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


print("================================================================")
print("STUDENT GRADING SYSTEM".center(60))
print("================================================================\n")

print("WELCOME!".center(60))
print("THIS IS THE SYSTEM'S MAIN DASHBOARD\n".center(60))

print("Choose an Option:")
print("A. Add a Student")
print("B. View Student Records")
print("C. Update/Change Student Records")
print("D. Delete Student Records")
print("E. Grade Status")
print("F. Dean's List")
print("G. Export Class Record")
print("H. Exit Program\n")
print("================================================================\n")


records = load_Records()


while True:
    choice = input("Enter your choice (A/B/C/D/E/F/G/H): ").strip().upper()
    try:
        if choice not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            raise ValueError("Invalid choice. Please select A, B, C, D, E, F, G, or H.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Kindly re-enter your choice.\n")
        print()
        continue



    if choice == 'A':
        student_name = input("\nEnter Student Name: ")
        if any(info["name"].lower() == student_name.lower() for info in records.values()):
            print(f"The name {student_name} was already added in the records\n")
            print()
            continue
        student_id = input("Enter Student ID: ")
        if student_id in records:
            print(f"{student_id} was already added in the records\n")
            print()
            continue

        print("\nEnter the Student's Grade for the following subjects")
        grade_Filipino = float(input("Filipino: "))
        grade_Communication = float(input("Communication: "))
        grade_History = float(input("History: "))
        grade_Calculus = float(input("Calculus: "))
        grade_Pathfit = float(input("PATHFIT: "))
        grade_Arts = float(input("Arts: "))

        records[student_id] = {
            "name": student_name,
            "grades": {
                "Filipino": grade_Filipino,
                "Communication": grade_Communication,
                "History": grade_History,
                "Calculus": grade_Calculus,
                "Pathfit": grade_Pathfit,
                "Arts": grade_Arts
            }
        }

        save_Records(records)
        average_grade = (grade_Filipino + grade_Communication + grade_History + grade_Calculus + grade_Pathfit + grade_Arts)/ 6
        print(f"\nStudent {student_name}; ID {student_id} with an Average of"
              f" {average_grade:.2f} has been added successfully to the Records\n")
        print()


    elif choice == 'B':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add and view the Records\n")
            print()
            continue

        print("\n======STUDENT RECORDS=====")
        for student_id, info in records.items():
            grades = info["grades"]
            average = sum(grades.values()) / len(grades)
            print(f"Name: {info['name']} | ID: {student_id}")
            for subject, score in grades.items():
                print(f" - {subject}: {score:.2f}")
            print(f"General Average: {average:.2f}\n")
            print()


    elif choice == 'C':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add and change/update the Records\n")
            print()
            continue

        print("\n===== STUDENT LIST =====")
        for student_id, info in records.items():
            print(f"ID: {student_id}\n")

        called_id = input("\nWhich one of these students would you like to change or update: ")
        if called_id in records:
            print(f"\nFound Student: {records[called_id]['name']}")
            print("GRADES:")
            for subject, score in records[called_id]["grades"].items():
                print(f" - {subject}: {score:.2f}")

            upd_subjects = input("\nWhich among his grades would you update: ")
            if upd_subjects in records[called_id]["grades"]:
                new_grade = float(input(f"Enter new grade for {upd_subjects}: "))
                records[called_id]["grades"][upd_subjects] = new_grade
                save_Records(records)
                print(f"\n{upd_subjects} has been changed to {new_grade:.2f}\n")
                print()
            else:
                print(f"\nSubject for {records[called_id]['name']} isn't found. Please check proper capitalization and spelling\n")
                print()
        else:
            print("\nStudent ID isn't found\n")
            print()


    elif choice == 'D':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add then remove a student from the Records\n")
            print()
            continue

        print("\n===== STUDENT LIST =====")
        for student_id, info in records.items():
            print(f"ID: {student_id}\n")

        remove_id = input("\nWhich one of these students would you like to remove: ")
        if remove_id in records:
            del records[remove_id]
            save_Records(records)
            print(f"\nStudent ID: {remove_id} has been removed")
            print("Check Option B. to see if the specific student is removed for double checking\n")
            print()
        else:
            print("\nStudent ID not found\n")
            print()


    elif choice == 'E':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add\n")
            print()
            continue

        print("\n===== STUDENT LIST =====")
        for called_id, info in records.items():
            print(f"ID: {called_id}\n")
        called_id = input("\nWhich one of these students would you like to know their Grade Status: ")

        if called_id in records:
            info = records[called_id]
            grades = info["grades"]
            average = sum(grades.values()) / len(grades)
            if average >= 75.0:
                print(f"Name: {info['name']} | ID: {called_id}")
                print("GRADE STATUS: PASS\n")
                print()
            else:
                print(f"Name: {info['name']} | ID: {called_id}")
                print("GRADE STATUS: FAIL\n")
                print()
        else:
            print("\nStudent ID isn't found\n")
            print()


    elif choice == 'F':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add\n")
            print()
            continue

        print("\n===== STUDENT LIST =====")
        for called_id, info in records.items():
            print(f"ID: {called_id}\n")
        called_id = input("\nWhich one of these students would you like to know is their in the Dean's List: ")
        
        if called_id in records:
            info = records[called_id]
            grades = info["grades"]
            honor = sum(grades.values()) / len(grades)
            if honor >= 90:
                print(f"\nCONGRATULATIONS!! {info['name']} YOU ARE PART OF THE HONORS LIST!!\n")
                print()
            else:
                print(f"\nTry again next sem {info['name']} YOU CAN DO IT!!\n")
                print()
        else:
            print("\nStudent ID isn't found\n")
            print()


    elif choice == 'G':
        if not records:
            print("\nNo students were added")
            print("Please pick Choice A. If you wish to add and make a Report\n")
            print()
            continue
        
        print("\n===== STUDENT LIST =====")
        for called_id, info in records.items():
            print(f"ID: {called_id}\n")
        export_id = input("\nWhich student do you want to export as a txt file?: ")

        if export_id in records:
            info = records[export_id]
            grades = info["grades"]
            filename = f"student_export_{export_id}.txt"
            with open(filename, "w") as report:
                report.write("====== STUDENT REPORT =======\n")
                report.write(f"Name: {info['name']}\n")
                report.write(f"Grades are listed below \n")
                for subjects, score in grades.items():
                    report.write(f"{subjects}: {score:.2f}\n")
                print("Check your file if the report is there\n")
                print()
        else:
            print("\nStudent ID isn't found\n")
            print()



    elif choice == 'H':
        print("\nTHANK YOU FOR USING THIS SYSTEM!!!")
        break;
