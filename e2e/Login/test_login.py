from seleniumbase import BaseCase

from e2e.main_objects.action_objects.login_action_object import validLogin
from helper.user_helper import B2B2C_URLS, USER, PASSWORDS


class TestLogin(BaseCase):
    url = B2B2C_URLS['LK-URL']
    email = USER['LK-USER']
    password = PASSWORDS['LK-PSS']

    def test_linkedin(self):

        self.visit(f"{self.url}")
        assert self.get_current_url() == f"{self.url}"
        validLogin.valid_login(self, email=self.email, password=self.password)
