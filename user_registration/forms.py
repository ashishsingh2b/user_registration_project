from django import forms
from .models import UserProfile, Hobby

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'hobbies': forms.CheckboxSelectMultiple(),  # Use CheckboxSelectMultiple for multiple selection
            'gender': forms.RadioSelect(),
            'remarks': forms.CheckboxInput(),
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hobbies'].queryset = Hobby.objects.all()
