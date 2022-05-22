from flask_mail import Message
from flask import current_app
from .mail import mail


def send_mail(message_data: dict):
    """
    This function uses the Google's smtp server service to send updates of the state of the requests
    from the user we configurate in the app to the email we pass as parameter.

    # Parameters:
        message_data: dict
            Dictionary with all the information to send the email

            # Contains:
                subject: str
                    - Email's subject (new request for the approvers and change of state for the customers)
                message_data: str
                    - Info about the request and a link to the form.
                emails: List[str]
                    - A list of emails to send the message.
    """

    msg = Message(message_data["subject"],
                  sender=current_app.config["MAIL_DEFAULT_SENDER"],
                  recipients=[email for email in message_data["emails"]],
                  body=message_data["message"]
                  )
    mail.send(message=msg)
