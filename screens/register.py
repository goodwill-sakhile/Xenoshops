from kivymd.uix.screen import MDScreen
import requests

class RegisterScreen(MDScreen):
    def register_user(self):
        username = self.ids.username.text
        password = self.ids.password.text
        response = requests.post("http://127.0.0.1:8000/api/register/", data={"username": username, "password": password})
        if response.status_code == 201:
            self.ids.message.text = "Registered! Please log in."
        else:
            self.ids.message.text = "Registration failed."
