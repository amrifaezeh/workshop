class validLogin:
    @staticmethod
    def valid_login(sb, email, password):
        sb.click("a[href='https://www.linkedin.com/login']")
        sb.type("#username", email)
        sb.type("#password", password)
        sb.click("button[aria-label='Sign in']")
