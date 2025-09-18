"""
student_records.py

Problem Statement:
------------------
Design a Student Records Manager using Python data structures:
- List: to store all student records
- Tuple: to represent individual student records (immutable)
- Set: to store unique subjects
- Dictionary: to map roll number → student details

Operations:
1. Add a new student record
2. Get student details by roll number
3. Find top scorer(s)
4. Maintain a set of unique subjects
5. Display all student records
"""


class StudentRecordsManager:
    def __init__(self):
        # list to store tuples (roll_no, name, marks)
        self.records = []

        # dict for fast roll_no → details lookup
        self.records_dict = {}

        # set to keep track of unique subjects
        self.subjects = set()

    def add_student(self, roll_no: int, name: str, marks: dict, subjects: list):
        """Add a new student record with marks (dict) and subjects (list)."""
        if roll_no in self.records_dict:
            print(f"Roll No{roll_no} already exists. Skipping")
            return

        total_marks = sum(marks.values())

        record = (roll_no, name, total_marks)

        self.records.append(record)

        self.records_dict[roll_no] = (name,marks)

        self.subjects.update(subjects)

        print(f"Added student: {name} (Roll No {roll_no})")


    def get_student(self, roll_no: int):
        """Return details of a student by roll number."""
        if roll_no not in self.records_dict:
            print(f"No stound found with Roll No {roll_no}")
            return None

        name,marks = self.records_dict[roll_no]
        return {"roll_no": roll_no, "name":name,",marks":marks}


    def find_top_scorer(self):
        """Find the student(s) with the highest total marks."""
        if not self.records:
            print("No records available")
            return []

        max_marks = max(record[2] for record in self.records)
        toppers = [record for record in self.records if record[2] == max_marks]
        return toppers

    def add_subjects(self, new_subjects: list):
        """Update the set of unique subjects offered in the class."""
        self.subjects.update(new_subjects)

    def display_all(self):
        """Display all student records neatly."""
        if not self.records:
            print("No student records to display.")
            return

        print("\nAll Student Records:")
        print("-" * 40)
        for roll_no, name, total in self.records:
            print(f"Roll No: {roll_no}, Name: {name}, Total Marks: {total}")
        print("-" * 40)

        print(f"Unique Subjects Offered: {self.subjects}")


if __name__ == "__main__":
    # Demo usage
    manager = StudentRecordsManager()

    # Add students
    manager.add_student(
        1, "Alice", {"Math": 90, "Science": 85, "English": 88}, ["Math", "Science", "English"]
    )
    manager.add_student(
        2, "Bob", {"Math": 78, "Science": 92, "English": 80}, ["Math", "Science", "English"]
    )
    manager.add_student(
        3, "Charlie", {"Math": 95, "Science": 90, "English": 93}, ["Math", "Science", "English"]
    )

    # Display all records
    manager.display_all()

    # Get student details
    print("\nDetails of Roll No 2:")
    print(manager.get_student(2))

    # Find top scorer
    print("\nTop Scorer(s):")
    toppers = manager.find_top_scorer()
    for roll_no, name, total in toppers:
        print(f"{name} (Roll No {roll_no}) with {total} marks")