from django import forms

from documentapp.models import Document


class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = ( 'termofuse_link', 'privacypolicy_link','announcement_link','email', 'kakaotalk','phonenumber')

        labels = {
            'termofuse_link': '이용 약관 노션',
            'privacypolicy_link': '개인정보처리방침 노션',
            'announcement_link': '공지사항 노션',
            'kakaotalk': '오픈 카카오톡',
            'email': '이메일 주소',
            'phonenumber': '고객센터 연락처',
        }

        widgets = {
            'termofuse_link': forms.Textarea(attrs={'class': 'textarea'}),
            'privacypolicy_link': forms.Textarea(attrs={'class': 'textarea'}),
            'announcement_link': forms.Textarea(attrs={'class': 'textarea'}),
            'kakaotalk': forms.Textarea(attrs={'class': 'textarea'}),
            'email': forms.Textarea(attrs={'class': 'textarea'}),
            'phonenumber' : forms.TextInput(attrs={'class': 'textinput'}),
        }