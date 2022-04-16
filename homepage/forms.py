from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={"class": "input100", "placeholder": "Adınız...", "name": "name"})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "input100", "placeholder": "E-mail adresiniz...", "name": "email"})
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "input100", "placeholder": "Mesajınız...", "name": "message"})
    )

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        subject = "Yeni bir e-mailiniz var"
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')

        msg = f"{name} with email {from_email} said: "
        msg += f"\n'{subject}'\n\n"
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=False,
        )
