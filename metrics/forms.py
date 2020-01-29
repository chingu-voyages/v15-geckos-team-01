from django import forms
from .models import  Goal, GoalOne, GoalTwo, GoalThree, Bookmarks


#---- TODO ITEMS --- #
class GoalForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'placeholder': 'My New TO DO item',
            'aria-label': 'Set a new To Do item',
            'aria-describedby': 'add-btn'
            }))
    class Meta:
        model = Goal
        fields =['text', 'user']


#--- SINGULAR GOALS ----#
class GoalONEForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'id': 'goal_1_input',
            'class':'form-control',
            'placeholder': 'Goal 1',
            'aria-label': ' set a new Goal 1.',
            'aria-describedby': 'add_goal1_btn'
            }))
    class Meta:
        model = GoalOne
        fields =['text', 'user']

class GoalTWOForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'id': 'goal_2_input',
            'class': 'form-control',
            'placeholder': 'Goal 2',
            'aria-label': 'Set a new goal 2. ',
            'aria-describedby': 'button-addon4'
            }))
    class Meta:
        model = GoalTwo
        fields =['text', 'user']

class GoalTHREEForm(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={
            'id': 'goal_3_input',
            'class': 'form-control',
            'placeholder': 'Goal 3',
            'aria-label': 'Set a new goal 3.',
            'aria-describedby': 'button-addon4'
            }))

    class Meta:
        model = GoalThree
        fields =['text', 'user']

#---   Bookmarks -----#
class Bookmark(forms.Form):
    alink = forms.URLField(max_length=130, required=True, label="The URL you wish to save")
    nickname = forms.CharField(max_length=40, required=True, label="A nickname to make it easier to find in the list")

    class Meta:
        model = Bookmarks
        fields =['alink', 'nickname', 'user']

