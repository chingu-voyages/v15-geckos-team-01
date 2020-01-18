from django import forms

class GoalForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'placeholder': 'My New Goal',
            'aria-label': 'Set a new Goal',
            'aria-describedby': 'add-btn'
            }))



