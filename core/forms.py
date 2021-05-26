from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea, label="Content of the post")
    activate = forms.BooleanField(required=False)
    author = forms.CharField(max_length=255)
    email = forms.EmailField(required=False, help_text="Add your email if want it to be displayed (Not required).")

    def __str__(self):
        return self.title