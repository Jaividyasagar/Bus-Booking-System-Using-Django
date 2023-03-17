from django import forms

class Ticket(forms.Form):
    busno = forms.IntegerField()
    CHOICES = (('Chennai','Chennai'),
            ('Villupuram','Villupuram'),
            ('Chengalpattu','Chengalpattu'),
            ('Select','Select'),)
    destination = forms.MultipleChoiceField(choices=CHOICES)
    # destination = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple())
    noofpersons = forms.IntegerField()
