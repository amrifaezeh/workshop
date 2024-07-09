"""
Base Selenium test classes that actual test cases must inherit from
All test cases be run against UAT servers' URLs. It Is **strongly**
suggested that you use Page Object model when creating your test cases.
"""
import datetime
import os
import random
import string
import time

from time import sleep
import pytz
from dateutil import relativedelta
from selenium.webdriver.remote.webelement import WebElement
from dateutil.parser import parse

# URLS
B2B2C_URLS = {
    'LK-URL': 'https://www.linkedin.com/',
}
USER = {
    "LK-USER": "amrifaezeh@gmail.com",
}

PASSWORDS = {
    "LK-PSS": "tigerthrone1",
}

class Utils:
    """General utility methods for writing test cases."""
    # driver = None  # Chrome web driver
    url = None  # UAT domain name
    max_timeout = 60

    # def logout(self):
    #     """log ot user of the back office"""
    #     self.driver.get(f'{self.url}/auth/logout')

    @staticmethod
    def short_wait():
        """Wait for 1 second."""
        time.sleep(2)

    @staticmethod
    def long_wait():
        """Wait for 5 second."""
        time.sleep(5)

    @staticmethod
    def longest_wait():
        """Wait for 10 second."""
        time.sleep(10)

    @staticmethod
    def wait_for(seconds):
        """Wait for N second.
        Normally, you should use either `short_wait()`, `long_wait()`, or `longest_wait()` methods.
        If they aren't long enough for your particular scenario, then use this method.
        However, It is sign that the code you're testing isn't optimized,
         and you should consider reporting it to developers.
        """
        time.sleep(seconds)

    @staticmethod
    def get_random_chars():
        """
        Return random characters with random length of 7 to 10.
        :return: Random characters.
        """
        letters = list(string.ascii_lowercase)
        size = random.randint(7, 10)
        random.shuffle(letters)
        return "".join(letters[:size])

    @staticmethod
    def get_random_email(cls):
        """
        Return an Email address consisting of random letters.
        :return: A randomized Email address
        """
        domain = random.choice(['com', 'org', 'co.uk', 'com.my'])
        return f"{cls.get_random_chars()}@Test.{domain}"

    @staticmethod
    def get_random_phone_number(prefix='+6'):
        """
        Return a phone number consisting of random numbers
        :param prefix: Prefix to prepend,e.g. +1, or set to an empty string for no prefix.
        :return: A randomized phone number.
        """
        numbers = random.randint(10**8, 10**9)
        return f"{prefix}0{numbers}"

    @staticmethod
    def get_random_number():
        """
        Return a phone number consisting of random numbers
        :return: A randomized phone number.
        """
        numbers = random.randint(10**8, 10**9)
        return f"{numbers}"

    @staticmethod
    def get_n_random_number(n=0):
        """
        Return random number with random length on N.
        :param n: the length of n.
        :return: Random numbers.
        """
        if n > 1:
            range_start = 1 ** (n - 1)
            range_end = (10 ** n) - 1
            return random.randint(range_start, range_end)
        else:
            return 0

    @staticmethod
    def parse_date(date_str: str):
        """
        Parse the date.
        """
        return parse(date_str, dayfrist=True)

    @staticmethod
    def send_break(element: WebElement, word, delay):
        """
        sometimes system needs delay for response ,like payment. at that time you need to use this method.
        :param element: Navigate to the elements.
        :param word: the word that you want to write.
        :param delay: time sleep between each word.
        :return: It will write the letters with delay.
        Usage:
        >>> def payment_page(self):
        >>>     self.send_break(self.driver.find_element(By.CSS_SELECTOR, "#accuntNumber"), "4242424242424242", 1)
        """
        for c in word:
            element.send_keys(c)
            sleep(delay)

    @staticmethod
    def get_x_date_form_today(fmt='%d/%m/%Y %H:%M:%S %p', x=0, y=0, z=0):
        """
        Return today's date.
        :param fmt: Date format, see https://strftime.org for refrence.
        :param x: day.
        :param y: month.
        :param z: year.
        :return: today's date as a string
        """
        today = datetime.date.today() + relativedelta.relativedelta(days=x, months=y, years=z)
        return datetime.date.strftime(today, fmt)

    @staticmethod
    def current_time():
        t = datetime.datetime.now()
        return t

    @staticmethod
    def current_timezone(country):
        """
        return Time zone for each country.
        :param country: the country symbol
        Usage:
        >>> b = Utils.current_timezone(country="NL").strftime('%-d %b %Y, %-I:%M')
        >>> print(b)
        >>> # return >> 16 Mar 2021, 4:35
        """
        list_countries = {
            "NL": "Europe/Amsterdam",
            "AU": "Australia/Sydney",
            "US": "America/New_york",
            "MY": "Asia/Kuala_Lumpur"
        }
        tz = pytz.timezone(list_countries[country])
        ct = datetime.datetime.now(tz=tz)
        return ct

    @staticmethod
    def scroll_to_bottom(sb):
        """
        scroll to the bottom of the page.
        :return: maximum scroll to the bottom of the page.
        """
        sb.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def dateToStr(d: datetime, fmt: str) -> str:
        return d.strftime(fmt.replace('%-', '%#') if os.name == 'nt' else fmt)

    @staticmethod
    def password_generator(size):
        """
        Return random password with random length on size.
        :param size: the length of n.
        :return: Random password.
        """
        symbols_list = ['@', '$', '!', '%', '*', '?', '&', '#', '+', '=']
        symbols = random.choice(symbols_list)
        characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
        password = ''.join(random.choice(characters) for i in range(size))

        return f"{password}{symbols}"
