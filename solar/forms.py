from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core.mail import send_mail


class CaptchaContactForm(forms.Form):
    email = forms.CharField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    def send_email(self):
        send_mail(self.cleaned_data['subject'],
                  self.cleaned_data['content'],
                  self.cleaned_data['email'],
                  [settings.MAIL_RECIPIENT],
                  fail_silently=False)
