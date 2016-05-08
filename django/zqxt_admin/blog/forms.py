from django import forms

class AddForm(froms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()
	
	