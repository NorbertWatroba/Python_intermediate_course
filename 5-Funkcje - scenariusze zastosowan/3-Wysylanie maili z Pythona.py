from smtplib import SMTP_SSL

to_email = ['example@example.com']
mail_host = input('email host: ')
user = input('email: ')
password = input('password: ')
mail_subject = 'Automatically sent email'
mail_body = '''
Hello,
this mail has been sent automatically, please do not reply to this message.
Have a wonderful day:)'''
message = f'''From: {user}
Subject: {mail_subject}
{mail_body}
'''
print(repr(message))
try:
    server = SMTP_SSL(mail_host, 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, to_email, message)
    server.close()
    print('email sent successfully!')
except:
    print('[ERROR] Could not sent the email!')
