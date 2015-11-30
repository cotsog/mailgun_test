import unittest
from sender import send_email_to_user

class SendEmailToUser(unittest.TestCase):
    def test(self):
        a = send_email_to_user('plepage.facebook@gmail.com', 
                                'test', 
                                '<b>test</b>',
                                test=True)

        self.assertEquals(a.status_code, 200)