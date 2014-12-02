from django.forms import ModelForm
from student.models import student_profile,faculty_profile,material
from django import forms
from student.models import Course
from ckeditor.widgets import CKEditorWidget


class student_profile_form(ModelForm):
	class Meta:
		model=student_profile
		fields=['DOB','Branch','Semester','image','coursetaken']

class faculty_profile_form(ModelForm):
	class Meta:
		model=faculty_profile
		fields=['department','facultyrating','areaofinterest','research','description','weburl','image']

class add_material_form(ModelForm):
	class Meta:
		model=material
		fields=['title','description','document']

class update_student_image(ModelForm):
	class Meta:
		model=student_profile
		fields=['image']

class update_faculty_image(ModelForm):
	class Meta:
		model=faculty_profile
		fields=['image']

class CourseForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(required=True)


    class Meta:
        model = Course