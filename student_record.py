import csv
import os

CSV_FILE = 'students.csv'
FIELDNAMES = ['Roll Number', 'Name', 'Age', 'Class']

def ensure_csv_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_student():
    roll = input('Enter Roll Number: ')
    name = input('Enter Name: ')
    age = input('Enter Age: ')
    student_class = input('Enter Class: ')
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({'Roll Number': roll, 'Name': name, 'Age': age, 'Class': student_class})
    print('Student added successfully!')

def view_students():
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        print(f"{'Roll Number':<15}{'Name':<20}{'Age':<5}{'Class':<10}")
        print('-'*50)
        for row in reader:
            print(f"{row['Roll Number']:<15}{row['Name']:<20}{row['Age']:<5}{row['Class']:<10}")

def search_student():
    roll = input('Enter Roll Number to search: ')
    found = False
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Roll Number'] == roll:
                print('Student found:')
                print(row)
                found = True
                break
    if not found:
        print('Student not found.')

def update_student():
    roll = input('Enter Roll Number to update: ')
    updated = False
    students = []
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Roll Number'] == roll:
                print('Enter new details (leave blank to keep current):')
                name = input(f"Name [{row['Name']}]: ") or row['Name']
                age = input(f"Age [{row['Age']}]: ") or row['Age']
                student_class = input(f"Class [{row['Class']}]: ") or row['Class']
                students.append({'Roll Number': roll, 'Name': name, 'Age': age, 'Class': student_class})
                updated = True
            else:
                students.append(row)
    if updated:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
        print('Student record updated.')
    else:
        print('Student not found.')

def delete_student():
    roll = input('Enter Roll Number to delete: ')
    deleted = False
    students = []
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Roll Number'] == roll:
                deleted = True
            else:
                students.append(row)
    if deleted:
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
        print('Student record deleted.')
    else:
        print('Student not found.')

def main():
    ensure_csv_exists()
    while True:
        print('\nStudent Record Management System')
        print('1. Add Student')
        print('2. View Students')
        print('3. Search Student')
        print('4. Update Student')
        print('5. Delete Student')
        print('6. Exit')
        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main() 