class Person:
    instances = []

    def __init__(self, name, subject=None):
        self.name = name
        self.subject = subject
        Person.instances.append(self)

    @classmethod
    def import_persons(cls, filename):
        persons = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(', ')
                if len(data) == 2:
                    name, subject = data
                    persons.append(Mitarbeiter(name, subject))
                elif len(data) == 1:
                    name = data[0]
                    persons.append(Kunde(name))
        return persons

    @classmethod
    def print_person_imports(cls, input_file):
        persons = cls.import_persons(input_file)
        for person in persons:
            if isinstance(person, Mitarbeiter):
                print(f"Name: {person.name}, Subject: {person.subject}")
            else:
                print(f"Name: {person.name}")

    @classmethod
    def add_person(cls, class_name, name, subject=None):
        person = class_name(name, subject) if subject else class_name(name)
        cls.instances.append(person)
        print(f"{class_name.__name__}: {name} added.") 
        for i in cls.instances:
            print(i)
            
        return person

    @classmethod
    def export_person_to_new_file(cls, filename, data):
        with open(filename, 'w', newline="") as file:
            for person in data:
                if isinstance(person, Mitarbeiter):
                    file.write(f"{person.name}, {person.subject}\n")
                else:
                    file.write(f"{person.name}\n")

    @classmethod
    def export_person_append(cls, filename, data):
        with open(filename, 'a', newline="") as file:
            for person in data:
                if isinstance(person, Mitarbeiter):
                    file.write(f"{person.name}, {person.subject}\n")
                else:
                    file.write(f"{person.name}\n")

    @classmethod
    def filter_person(cls, names, persons):
        for person in persons:
            if person in names:
                print(person)


class Mitarbeiter(Person):
    def __init__(self, name, subject):
        super().__init__(name, subject)


class Kunde(Person):
    def __init__(self, name):
        super().__init__(name)


class Course:
    instances = []
    def __init__(self, title, teacher, duration):
        self.title = title
        self.teacher = teacher
        self.duration = duration

    def export_course(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.title}, {self.teacher}, {self.duration}\n")

