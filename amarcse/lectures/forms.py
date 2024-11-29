from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['lecture_name', 'notes', 'video', 'image']  # Ensure all model fields are included

    # Optional: Add custom validation for each field if necessary
    def clean_lecture_name(self):
        name = self.cleaned_data.get('lecture_name')
        if not name:
            raise forms.ValidationError('This field is required')

        return name

from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['question_file', 'answer_file']