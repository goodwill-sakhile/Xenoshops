from kivymd.uix.screen import MDScreen
import requests
from kivymd.uix.list import OneLineListItem

class ShopListScreen(MDScreen):
    def on_enter(self):
        self.ids.shop_list.clear_widgets()
        response = requests.get("http://127.0.0.1:8000/api/shops/")
        data = response.json()
        for shop in data:
            item = OneLineListItem(text=shop['name'], on_release=lambda x, shop=shop: self.show_details(shop))
            self.ids.shop_list.add_widget(item)

    def show_details(self, shop):
        self.manager.get_screen('shop_detail').shop_data = shop
        self.manager.current = 'shop_detail'
