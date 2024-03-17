import random

from prettytable import PrettyTable

from student import read_students, Student
from professional import Professional, read_professionals

groups = 0


class SeatingArrangement:
    @staticmethod
    def exists_in_table(person, table):
        for p in table:
            if str(p) == str(person):
                return True
        return False

    def __init__(self, total_tables):
        self.student_list = []
        self.professional_list = []
        self.tables = [[] for _ in range(total_tables)]
        self.rotation2 = [[] for _ in range(total_tables)]
        self.rotation3 = [[] for _ in range(total_tables)]
        self.total_tables = total_tables

        # Populate student list (Assuming it's loaded from file or another source)
        # Add your student objects here
        self.student_list = read_students("students.csv")

        # Populate professional list (Assuming it's loaded from file or another source)
        # Add your professional objects here
        self.professional_list = read_professionals("professionals.csv")

    import random

    def assign_tables(self):
        # Assign professionals to tables in rotation 1
        for professional in self.professional_list:
            added = False
            for i in range(self.total_tables):
                if len(self.tables[i]) == 0:
                    self.tables[i].append(professional)
                    added = True
                    break
                elif len(self.tables[i]) == 1 and self.tables[i][0].company == professional.company:
                    self.tables[i].append(professional)
                    added = True
                    break
            if not added:
                for i in range(self.total_tables):
                    if len(self.tables[i]) == 1:
                        self.tables[i].append(professional)
                        added = True
                        break

        # Assign students to tables in rotation 1
        for student in self.student_list:
            added = False
            for i in range(self.total_tables):
                if len(self.tables[i]) < 6:
                    test = self.tables[i][0]
                    if test.company in student.companies:
                        self.tables[i].append(student)
                        student.companies.remove(test.company)
                        added = True
                        break
                    if len(self.tables[i]) > 1 and isinstance(self.tables[i][1], Professional):
                        test2 = self.tables[i][1]
                        if test2.company in student.companies:
                            self.tables[i].append(student)
                            added = True
                            break
            if not added:
                for i in range(self.total_tables):
                    if len(self.tables[i]) < 8:
                        self.tables[i].append(student)
                        added = True
                        break

        # Shuffle the student list
        random.shuffle(self.student_list)

        # Assign students to rotation 2
        for student in self.student_list:
            assigned = False
            for i in range(self.total_tables):
                if student not in self.tables[i] and len(self.rotation2[i]) < 6:
                    self.rotation2[i].append(student)
                    assigned = True
                    break
            if assigned:
                continue

        # Shuffle the student list again for rotation 3
        random.shuffle(self.student_list)

        # Assign students to rotation 3
        for student in self.student_list:
            assigned = False
            for i in range(self.total_tables):
                if student not in self.tables[i] and student not in self.rotation2[i] and len(self.rotation3[i]) < 6:
                    self.rotation3[i].append(student)
                    assigned = True
                    break
            if assigned:
                continue

    def print_tables(self):
        # 2D list to store student names and their corresponding rotation numbers
        student_data = [["" for _ in range(3)] for _ in range(len(self.student_list))]

        # Populate student_data with rotation numbers
        for i in range(self.total_tables):
            for person in self.tables[i]:
                if isinstance(person, Student):
                    student_data[self.student_list.index(person)][0] = i + 1
        for i in range(self.total_tables):
            for person in self.rotation2[i]:
                if isinstance(person, Student):
                    student_data[self.student_list.index(person)][1] = i + 1
        for i in range(self.total_tables):
            for person in self.rotation3[i]:
                if isinstance(person, Student):
                    student_data[self.student_list.index(person)][2] = i + 1

        # Print table for students
        student_table = PrettyTable()
        student_table.field_names = ["Student Name", "ID Number", "Rotation 1", "Rotation 2", "Rotation 3"]
        for i, student in enumerate(self.student_list):
            student_table.add_row([student.name, student.id] + student_data[i])
        print("Students:")
        print(student_table)

    def print_professional_tables(self):
        # Print table for professionals
        professional_table = PrettyTable()
        professional_table.field_names = ["Professional Name", "Company", "Table Number"]
        for i in range(self.total_tables):
            for person in self.tables[i]:
                if isinstance(person, Professional):
                    professional_table.add_row([person.name, person.company, i + 1])
        print("\nProfessionals:")
        print(professional_table)

    def print_table_summary(self):
        print("Table Summary:")
        print("Rotation 1:")
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}: {len(table)} people")

        print("\nRotation 2:")
        for i, table in enumerate(self.rotation2):
            print(f"Table {i + 1}: {len(table)} people")

        print("\nRotation 3:")
        for i, table in enumerate(self.rotation3):
            print(f"Table {i + 1}: {len(table)} people")


def main():
    print("Welcome to the Group Assignment Program")
    groups = int(input("Enter the number of groups: "))
    seating_arrangement = SeatingArrangement(groups)
    seating_arrangement.assign_tables()
    while True:
        print("\nMenu:")
        print("1. Print Student table")
        print("2. print Professional table")
        print("3. print table summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            seating_arrangement.print_tables()
        elif choice == "2":
            seating_arrangement.print_professional_tables()
        elif choice == "3":
            seating_arrangement.print_table_summary()
        elif choice == "4":
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Example usage:
# seating_arrangement = SeatingArrangement()
# seating_arrangement.assign_tables()
# seating_arrangement.print_tables()

if __name__ == "__main__":
    main()
