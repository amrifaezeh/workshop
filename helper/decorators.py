from functools import wraps

import allure
from allure_commons.types import AttachmentType


def seleniumbase_class_func_exception_handler(name="Error"):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                val = func(self, *args, **kwargs)
                return val
            except Exception:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=name,
                    attachment_type=AttachmentType.PNG,
                )
                assert False

        return wrapper

    return decorator
