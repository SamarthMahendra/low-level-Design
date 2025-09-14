class SMTPServer:

    def connect(self):
        print("Connecting to SMTP server...")

    def disconnect(self):
        print("Disconnecting from SMTP server...")


class Authenticator:

    def authenticate(self, user, password):
        print(f"Authenticating user {user}...")
        # Simulate authentication logic
        if user == "admin" and password == "password":
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False


class EmailFormatter:

    def format(self, subject, body):
        print("Formatting email...")
        return f"Subject: {subject}\n\n{body}"

class Logger:

    def log(self, message):
        print(f"Log: {message}")

class EmailClientFacade:

    def __init__(self, user, password):
        self.smtp_server = SMTPServer()
        self.authenticator = Authenticator()
        self.formatter = EmailFormatter()
        self.logger = Logger()
        self.user = user
        self.password = password
        self.connected = False

    def send_email(self, to, subject, body):
        if not self.connected:
            self.smtp_server.connect()
            if not self.authenticator.authenticate(self.user, self.password):
                self.logger.log("Failed to authenticate. Email not sent.")
                return
            self.connected = True

        formatted_email = self.formatter.format(subject, body)
        print(f"Sending email to {to}:\n{formatted_email}")
        self.logger.log(f"Email sent to {to} with subject '{subject}'.")

    def disconnect(self):
        if self.connected:
            self.smtp_server.disconnect()
            self.connected = False
            self.logger.log("Disconnected from SMTP server.")



# Client code
if __name__ == "__main__":
    email_client = EmailClientFacade("admin", "password")
    email_client.send_email("example@gamil.com", "Test Subject", "This is a test email body.")
    email_client.disconnect()
