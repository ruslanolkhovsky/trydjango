from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'description',
        ]

    # Validation methods
    # def clean_<fieldname>(self):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "@" in name:
            raise forms.ValidationError("No @ is allowed in the name!")
        return name
