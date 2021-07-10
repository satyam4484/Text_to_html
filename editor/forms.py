from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget

class editorform(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label_suffix='',label='')
    class Meta:
        model = Editor
        fields="__all__"