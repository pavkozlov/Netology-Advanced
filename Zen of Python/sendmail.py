import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender:
    def __init__(self, login, password, subject, recipient, message):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = list()
        self.recipients.append(recipient)
        self.message = message
        self.header = None

    def send_mail(self):
        msg = MIMEMultipart()
        msg["From"] = self.login
        msg["To"] = ', '.join(self.recipients)
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, msg["To"], self.message)

        ms.quit()

    def recieve_message(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        if self.header:
            criterion = f"(HEADER Subject '{self.header}')"
        else:
            criterion = f"(HEADER Subject 'ALL')"

        result, data = mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = (data[0][1]).decode(encoding="utf-8")
        email_message = email.message_from_string(raw_email)
        mail.logout()

        print(email_message)


if __name__ == "__main__":
    test = MailSender("it.pavelkozlov@gmail.com", "******", "Theme 1", "it.pavelkozlov@gmail.com", "hello world")
    test.send_mail()
    test.recieve_message()
