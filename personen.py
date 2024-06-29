class Member:
    instances = []

    def __init__(self, name, subject=None):
        self.name = name
        self.subject = subject
        Member.instances.append(self)

    @classmethod
    def import_Members(cls, filename):
        Members = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(', ')
                if len(data) == 2:
                    name, subject = data
                    Members.append(Official(name, subject))
                elif len(data) == 1:
                    name = data[0]
                    Members.append(Ordinary(name))
        return Members

    @classmethod
    def print_Member_imports(cls, input_file):
        Members = cls.import_Members(input_file)
        for Member in Members:
            if isinstance(Member, Official):
                print(f"Name: {Member.name}, Subject: {Member.subject}")
            else:
                print(f"Name: {Member.name}")

    @classmethod
    def add_Member(cls, class_name, name, subject=None):
        Member = class_name(name, subject) if subject else class_name(name)
        cls.instances.append(Member)
        print(f"{class_name.__name__}: {name} added.") 
        for i in cls.instances:
            print(i)
            
        return Member

    @classmethod
    def del_Member(cls, name):
        for instance in cls.instances:
            if instance.name == name:
                cls.instances.remove(instance)
                print(f"Member {name} deleted succesfully.")
                return
        print(f"Member {name} not found.")

    @classmethod
    def export_Member_to_new_file(cls, filename, data):
        with open(filename, 'w', newline="") as file:
            for Member in data:
                if isinstance(Member, Official):
                    file.write(f"{Member.name}, {Member.subject}\n")
                else:
                    file.write(f"{Member.name}\n")

    @classmethod
    def export_Member_append(cls, filename, data):
        with open(filename, 'a', newline="") as file:
            for Member in data:
                if isinstance(Member, Official):
                    file.write(f"{Member.name}, {Member.subject}\n")
                else:
                    file.write(f"{Member.name}\n")

    @classmethod
    def filter_Member(cls, names, Members):
        for Member in Members:
            if Member in names:
                print(Member)


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
        with open(filename, 'a') as file:
            file.write(f"{self.title}, {self.teacher}, {self.duration}\n")

