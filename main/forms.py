from django import forms

class EngineSearchForm(forms.Form):
    engine_name = forms.CharField(label='', max_length=100)

class EngineConditionForm(forms.Form):
    CHOICES = (
        ('new', 'Новый'),
        ('used', 'Б/у'),
    )

    condition = forms.MultipleChoiceField(label='', choices=CHOICES, widget=forms.CheckboxSelectMultiple, error_messages="")