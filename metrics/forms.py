from django import forms


#---- TODO ITEMS --- #
class GoalForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'placeholder': 'My New TO DO item',
            'aria-label': 'Set a new To Do item',
            'aria-describedby': 'add-btn'
            }))


#--- SINGULAR GOALS ----#
class GoalONEForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Goal 1',
            'aria-label': ' set a new Goal 1.',
            'aria-describedby': 'button-addon4'
            }))

class GoalTWOForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Goal 2.',
            'aria-label': 'Set a new goal 2. ',
            'aria-describedby': 'button-addon4'
            }))

class GoalTHREEForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'My new Third Goal.',
            'aria-label': 'Set a new goal 3.',
            'aria-describedby': 'button-addon4'
            }))
