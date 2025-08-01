from kivymd.uix.screen import MDScreen
import requests

class LoginScreen(MDScreen):
    def login_user(self):
        username = self.ids.username.text
        password = self.ids.password.text
        response = requests.post("http://127.0.0.1:8000/api/auth/", data={'username': username, 'password': password})
        if response.status_code == 200:
            token = response.json()['token']
            self.manager.parent.token = token  # save globally
            self.manager.current = 'home'
        else:
            self.ids.error.text = "Login failed. Check credentials."
