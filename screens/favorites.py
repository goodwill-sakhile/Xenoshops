from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
import requests

class FavoritesScreen(MDScreen):
    def on_enter(self):
        token = self.manager.parent.token
        headers = {'Authorization': f'Token {token}'}
        response = requests.get("http://127.0.0.1:8000/api/favorites/", headers=headers)
        self.ids.favorite_list.clear_widgets()
        for item in response.json():
            shop_name = item['shop']
            self.ids.favorite_list.add_widget(OneLineListItem(text=shop_name))
