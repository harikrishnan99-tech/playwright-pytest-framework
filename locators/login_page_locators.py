from utils.csv_reader import read_text_values

text_values = read_text_values("wordings_data.csv")
class LoginLocators:
    USERNAME_INPUT = "input[name='user-name']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "input[type='submit']"
    TITLE_TEXT = f"text={text_values.get('homepagetitle', '')}"

