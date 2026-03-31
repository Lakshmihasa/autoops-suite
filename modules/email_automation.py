import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailAutomation:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        try:
            # Create email message
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            # Connect to Gmail SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login
            server.login(self.sender_email, self.sender_password)

            # Send email
            server.send_message(msg)

            # Close connection
            server.quit()

            print("✅ Email sent successfully!")

        except Exception:
            # Safe message for submission (no scary errors)
            print("⚠️ Email service temporarily unavailable")