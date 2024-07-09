class validLogin:
    @staticmethod
    def valid_login(sb, email, password):
        sb.type("#username", email)
        sb.type("#password", password)
        sb.click("button[aria-label='Sign in']")
