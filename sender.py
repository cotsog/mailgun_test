import requests
import settings

def send_email_to_user(user_email, subject, body, test=False):
    """
    Send an email to an user

    :param string user_email: User's email
    :param string subject: Email's topic
    :param string body: HTML Body
    """
    return requests.post(settings.MAILGUN_API_URL,
                        auth=("api", settings.MAILGUN_API_KEY),
                        data={"from": settings.FROM_EMAIL,
                              "to": [user_email],
                              "subject": subject,
                              "html": body,
                              "o:testmode": True if test else test})
