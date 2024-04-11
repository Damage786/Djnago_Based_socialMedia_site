from django.core.mail import get_connection
from django.core.mail.message import EmailMessage

try:
    connection = get_connection(
        host='smtp.gmail.com',
        port=587,
        username='anveshs851@gmail.com',
        password='123@gmail.com@#',
        use_tls=True,
    )

    email = EmailMessage(
        subject='Test Email',
        body='This is a test email.',
        from_email='anveshs851@gmail.com',
        to=['recipient@example.com'],
        connection=connection,
    )
    
    # Attempt to send the email
    result = email.send()
    print("Email sent successfully:", result)

except Exception as e:
    print("Error sending email:", str(e))
