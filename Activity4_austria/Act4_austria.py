class StudentRecordManager:
    def __init__(self):
        self.records = []
        self.file_path = None

    def open_file(self, path):
        try:
            with open(path, 'r') as file:
                self.records = [tuple(line.strip().split(',')) for line in file]
            self.file_path = path
            print("File loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                for record in self.records:
                    file.write(','.join(record) + '\n')
            print("File saved successfully.")
        else:
            print("No file path specified. Use 'Save As' instead.")

    def save_as_file(self, path):
        with open(path, 'w') as file:
            for record in self.records:
                file.write(','.join(record) + '\n')
        self.file_path = path
        print("File saved successfully.")

    def show_all_students(self):
        for record in self.records:
            print(record)

    def order_by_last_name(self):
        def last_name_key(record):
            return record[1].split()[1]
        self.records.sort(key=last_name_key)
        self.show_all_students()

    def order_by_grade(self):
        def grade_key(record):
            return 0.6 * float(record[2]) + 0.4 * float(record[3])
        self.records.sort(key=grade_key, reverse=True)
        self.show_all_students()

    def show_student_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Student not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):
        self.records.append((student_id, first_name + ' ' + last_name, class_standing, major_exam))
        print("Record added successfully.")

    def edit_record(self, student_id, new_class_standing, new_major_exam):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                self.records[i] = (record[0], record[1], new_class_standing, new_major_exam)
                print("Record updated successfully.")
                return
        print("Student not found.")

    def delete_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                self.records.remove(record)
                print("Record deleted successfully.")
                return
        print("Student not found.")

    def menu(self):
        while True:
            print("\nStudent Record Management")
            print("1. Open File")
            print("2. Save File")
            print("3. Save As File")
            print("4. Show All Students")
            print("5. Order by Last Name")
            print("6. Order by Grade")
            print("7. Show Student Record")
            print("8. Add Record")
            print("9. Edit Record")
            print("10. Delete Record")
            print("11. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                path = input("Enter file path: ")
                self.open_file(path)
            elif choice == '2':
                self.save_file()
            elif choice == '3':
                path = input("Enter file path: ")
                self.save_as_file(path)
            elif choice == '4':
                self.show_all_students()
            elif choice == '5':
                self.order_by_last_name()
            elif choice == '6':
                self.order_by_grade()
            elif choice == '7':
                student_id = input("Enter Student ID: ")
                self.show_student_record(student_id)
            elif choice == '8':
                student_id = input("Enter Student ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                class_standing = input("Enter Class Standing Grade: ")
                major_exam = input("Enter Major Exam Grade: ")
                self.add_record(student_id, first_name, last_name, class_standing, major_exam)
            elif choice == '9':
                student_id = input("Enter Student ID: ")
                new_class_standing = input("Enter New Class Standing Grade: ")
                new_major_exam = input("Enter New Major Exam Grade: ")
                self.edit_record(student_id, new_class_standing, new_major_exam)
            elif choice == '10':
                student_id = input("Enter Student ID: ")
                self.delete_record(student_id)
            elif choice == '11':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = StudentRecordManager()
    manager.menu()