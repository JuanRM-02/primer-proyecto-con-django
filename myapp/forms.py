from django import forms


class Create_new_task(forms.Form):
    title = forms.CharField(label='Titulo', max_length=200, required=True, 
                            widget=forms.TextInput({'class': 'input'}))
    description = forms.CharField(label='Descripcion', widget=forms.Textarea({'class': 'input'}))



class Create_new_project(forms.Form):
    name = forms.CharField(label='Nombre', max_length=200, required=True)