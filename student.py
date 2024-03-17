import csv


class Student:
    def __init__(self, name, id, companies):
        self.name = name
        self.id = id
        self.companies = companies.split(", ")

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_companies(self):
        return self.companies

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id}, Companies: {', '.join(self.companies)}"


def read_students(file_name):
    students = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, id, companies = row
            students.append(Student(name.strip(), id.strip(), companies.strip()))
    return students


# # Example usage:
# students = read_students("students.csv")
# for student in students:
#     print(student)
