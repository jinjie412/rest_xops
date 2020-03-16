from django.core.mail import EmailMessage
from django.conf import settings

def file_mail(bak_name, subject, email_from, email_to):
    '''发送附件'''
    email = EmailMessage(
        subject,
        'Body goes here',
        email_from,   # 发件人
        email_to,   # 收件人
        headers={'Message-ID': 'foo'},
    )
    email.attach_file(bak_name, mimetype=None)
    email.send()