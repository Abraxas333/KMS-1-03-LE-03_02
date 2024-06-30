import csv

class Member:
    instances = []

    def __init__(self, name, subject=None):
        self.name = name
        self.subject = subject
        Member.instances.append(self)

    @classmethod
    def import_Members(cls, filename):
        cls.instances.clear()  # Clear existing instances to avoid duplication
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, subject = row
                    cls.instances.append(Official(name, subject))
                elif len(row) == 1:
                    name = row[0]
                    cls.instances.append(Ordinary(name))
        return cls.instances

    @classmethod
    def print_Member_imports(cls, input_file):
        members = cls.import_Members(input_file)
        for member in members:
            if isinstance(member, Official):
                print(f"Name: {member.name}, Subject: {member.subject}")
            else:
                print(f"Name: {member.name}")

    @classmethod
    def add_Member(cls, class_name, name, subject=None):
        member = class_name(name, subject) if subject else class_name(name)
        print(f"{class_name.__name__}: {name} added.")
        for i in cls.instances:
            print(f"Name: {i.name}, Subject: {i.subject if hasattr(i, 'subject') else 'N/A'}")
        return member

    @classmethod
    def del_Member(cls, name):
        for instance in cls.instances:
            if instance.name == name:
                cls.instances.remove(instance)
                print(f"Member {name} deleted successfully.")
                return
        print(f"Member {name} not found.")

    @classmethod
    def export_Member_to_new_file(cls, filename, data):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for member in data:
                if isinstance(member, Official):
                    writer.writerow([member.name, member.subject])
                else:
                    writer.writerow([member.name])

    @classmethod
    def export_Member_append(cls, filename, data):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            for member in data:
                if isinstance(member, Official):
                    writer.writerow([member.name, member.subject])
                else:
                    writer.writerow([member.name])

    @classmethod
    def filter_Member(cls, names, members):
        for member in members:
            if member.name in names:
                print(f"Name: {member.name}, Subject: {member.subject if hasattr(member, 'subject') else 'N/A'}")


class Official(Member):
    def __init__(self, name, subject):
        super().__init__(name, subject)


class Ordinary(Member):
    def __init__(self, name):
        super().__init__(name)


class Course:
    instances = []

    def __init__(self, title, teacher, duration):
        self.title = title
        self.teacher = teacher
        self.duration = duration

    def export_course(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.title, self.teacher, self.duration])
