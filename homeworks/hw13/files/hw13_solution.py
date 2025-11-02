# pylint: disable=unspecified-encoding


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.group_stats = {}

    def create_students_file(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
        except IOError as e:
            print(f'Error while creating a file: {e}')

    def read_students_file(self):
        self.students = []
        self.group_stats = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    try:
                        name, group, grade_str = [x.strip() for x in line.split(',')]
                        grade = int(grade_str)
                        self.students.append((name, group, grade))
                        if group not in self.group_stats:
                            self.group_stats[group] = {'count': 0, 'total_grade': 0}
                        self.group_stats[group]['count'] += 1
                        self.group_stats[group]['total_grade'] += grade
                    except ValueError:
                        print(f'Incorrect format: {line}')
        except FileNotFoundError:
            print('File not found')
        except IOError as e:
            print(f'Error while reading a file: {e}')
        return self.students, self.group_stats

    def get_summary(self):
        summary = {}
        for group, stats in self.group_stats.items():
            avg = round(stats['total_grade'] / stats['count'], 1)
            summary[group] = {'count': stats['count'], 'avg_grade': avg}
        return summary

    def write_summary_to_file(self):
        try:
            with open(self.filename, 'a') as file:
                file.write(f'\nTotal students: {len(self.students)}\n')
                for group, stats in self.get_summary().items():
                    file.write(f"{group}: count = {stats['count']}, "
                               f"average grade = {stats['avg_grade']}\n")
        except IOError as e:
            print(f'Error while writing to file: {e}')
