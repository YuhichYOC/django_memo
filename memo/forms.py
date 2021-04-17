from django import forms


class Node(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w100',
        }),
    )
    text = forms.CharField(
        label='本文',
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'w100',
        }),
    )
