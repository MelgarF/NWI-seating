import csv

class Professional:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f"Professional: {self.name}, Company: {self.company}"

def read_professionals(file_name):
    professionals = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, company = row
            professionals.append(Professional(name.strip(), company.strip()))
    return professionals

# Example usage:
# professionals = read_professionals("professionals.csv")
# for professional in professionals:
#     print(professional)
