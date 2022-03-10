from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from sch_progs.models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        exclude = ['checked','vev']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
# self.helper.layout = Layout(
#     'email',
#     'password',
#     'remember_me',
#     StrictButton('Sign in', css_class='btn-default'),
# )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Αποθήκευση'))