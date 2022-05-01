import smtplib
from email.message import EmailMessage
from string import Template


class SendEmail:
    def __init__(self, name, surname, email, phone, question):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.question = question
        self.password = ''
        self.send()

    def send(self):
        with open('transport/templates/question.html', 'r') as f:
            html = f.read()

        template = Template(html)
        email = EmailMessage()
        email['from'] = 'Client'
        email['to'] = ''
        email['subject'] = 'Client Question'

        email.set_content(template.substitute({'name': f'{self.name}', 'surname': f'{self.surname}', 'phone': f'{self.phone}', 'email': f'{self.email}', 'question': f'{self.question}'}), 'html')

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user='', password=self.password)
            smtp.send_message(email)