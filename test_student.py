import unittest

students = []

# Functions
def add_student(name, roll, department):
    student = {
        "name": name,
        "roll": roll,
        "department": department
    }
    students.append(student)


def view_students():
    return students


def search_student(roll):
    for s in students:
        if s["roll"] == roll:
            return True
    return False


def update_student(roll, new_name, new_department):
    for s in students:
        if s["roll"] == roll:
            s["name"] = new_name
            s["department"] = new_department
            return True
    return False


def delete_student(roll):
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            return True
    return False


# Test Class
class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        students.clear()
        add_student("Ali", "101", "CS")

    # Add Student Test
    def test_add_student(self):
        add_student("Ahmed", "102", "SE")
        self.assertEqual(len(students), 2)

    # View Students Test
    def test_view_students(self):
        result = view_students()
        self.assertEqual(len(result), 1)

    # Search Student Test
    def test_search_student(self):
        self.assertTrue(search_student("101"))

    # Invalid Search Test
    def test_invalid_search(self):
        self.assertFalse(search_student("999"))

    # Update Student Test
    def test_update_student(self):
        result = update_student("101", "Ali Khan", "IT")
        self.assertTrue(result)

    # Delete Student Test
    def test_delete_student(self):
        result = delete_student("101")
        self.assertTrue(result)

    # Invalid Delete Test
    def test_invalid_delete(self):
        self.assertFalse(delete_student("999"))


if __name__ == '__main__':
    unittest.main()