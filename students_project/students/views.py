import random
from django.shortcuts import render


first_names = [
    "John", "Jane", "Michael", "Sarah", "David",
    "Emily", "Daniel", "Laura", "Matthew", "Sophia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"
]

def get_random_students():
    students = []
    for _ in range(100):
        student = {
            'name': random.choice(first_names),  
            'surname': random.choice(last_names), 
            'course': random.randint(1, 4)  
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    selected_student = random.choice(students)
    return render(request, 'students/main_page.html', {'student': selected_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students/students_page.html', {'students': students})
