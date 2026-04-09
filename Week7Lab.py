class AttendanceSystem:

    def __init__(self):
        self.students = []   # list to store student records
        self.student_id = 1000   # starting ID

    # 1. Add student
    def add_student(self):
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        attendance = float(input("Enter attendance percentage: "))

        self.student_id += 1

        # store as tuple (id, name, course, attendance)
        student = (self.student_id, name, course, attendance)
        self.students.append(student)

        print("Student added! ID:", self.student_id)

    # 2. Display students
    def display_students(self):
        if not self.students:
            print("No records found.")
            return

        print("\n--- Student Records ---")
        for s in self.students:
            print("ID:", s[0])
            print("Name:", s[1])
            print("Course:", s[2])
            print("Attendance:", str(s[3]) + "%")
            print("----------------------")

    # 3. Update student
    def update_student(self):
        sid = int(input("Enter student ID to update: "))
        found = False

        for i in range(len(self.students)):
            if self.students[i][0] == sid:
                found = True

                name = self.students[i][1]
                course = self.students[i][2]
                attendance = self.students[i][3]

                print("Student found:", name)

                new_course = input("Enter new course (leave blank to keep same): ")
                new_attendance = input("Enter new attendance (leave blank to keep same): ")

                if new_course:
                    course = new_course
                if new_attendance:
                    attendance = float(new_attendance)

                # update tuple
                self.students[i] = (sid, name, course, attendance)

                print("Record updated!")
                break

        if not found:
            print("Student not found!")

    # 4. Average attendance
    def average_attendance(self):
        if not self.students:
            print("No data available.")
            return

        total = 0
        for s in self.students:
            total += s[3]

        avg = total / len(self.students)
        print("Average Attendance:", round(avg, 2), "%")

    # Menu
    def menu(self):
        while True:
            print("\n--- Attendance System ---")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Update Student")
            print("4. Average Attendance")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.average_attendance()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")


# Run program
system = AttendanceSystem()
system.menu()