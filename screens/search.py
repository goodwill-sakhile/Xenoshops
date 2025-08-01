from kivymd.uix.screen import MDScreen
import requests
from kivymd.uix.list import OneLineListItem

class SearchScreen(MDScreen):
    def search_shops(self, query):
        self.ids.search_results.clear_widgets()
        if not query:
            return
        response = requests.get(f"http://127.0.0.1:8000/api/shops/?search={query}")
        data = response.json()
        for shop in data:
            item = OneLineListItem(text=shop['name'], on_release=lambda x, shop=shop: self.show_details(shop))
            self.ids.search_results.add_widget(item)

    def show_details(self, shop):
        self.manager.get_screen('shop_detail').shop_data = shop
        self.manager.current = 'shop_detail'
