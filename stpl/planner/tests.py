from django.test import TestCase
from .models import Student, Classes, Schedule
from .forms import ClassForm
from django.urls import reverse

# Create your tests here.

class StudentTest(TestCase):
    def test_stringOutput(self):
        student=Student(studentname='asdf')
        self.assertEqual(str(student), student.studentname)

    def test_tablename(self):
        self.assertEqual(str(Student._meta.db_table), 'student')

class ClassesTest(TestCase):
    def test_stringOutput(self):
        classes=Classes(classname='WEB PROGRAMMING: PYTHON')
        self.assertEqual(str(classes), classes.classname)

    def test_tablename(self):
        self.assertEqual(str(Classes._meta.db_table), 'classes')

class ScheduleTest(TestCase):
    def test_stringOutput(self):
        schedule=Schedule(schedulecomments='asdf')
        self.assertEqual(str(schedule), schedule.schedulecomments)

    def test_tablename(self):
        self.assertEqual(str(Schedule._meta.db_table), 'schedule')

class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planner/index.html')

class New_Class_Form_Test(TestCase):

    def test_ClassForm_is_valid(self):
        form = ClassForm(data={'classname': "SYSTEMS ANALYSIS", 'classid': "ITC 255", 'classinstructor': "Conger", 'classtime': "1:00pm", 'classdescription':"Analyze complex systems for development using various tools and approaches that reflect current industry practices. Prerequisite completion of ITC 110 with a minimum 2.0 or permission." })
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = ClassForm(data={'classname': "SYSTEMS ANALYSIS", 'classid': "ITC 255", 'classinstructor': "Conger", 'classtime': "1:00pm", 'classdescription':"Analyze complex systems for development using various tools and approaches that reflect current industry practices. Prerequisite completion of ITC 110 with a minimum 2.0 or permission." })
        self.assertFalse(form.is_valid())