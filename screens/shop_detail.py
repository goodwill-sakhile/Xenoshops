from kivymd.uix.screen import MDScreen
import requests
import webbrowser

def open_in_maps(self):
    address = self.shop_data['address'].replace(" ", "+")
    url = f"https://www.google.com/maps/search/?api=1&query={address}"
    webbrowser.open(url)

def on_enter(self):
    shop = self.shop_data
    self.ids.details_label.text = f"Name: {shop['name']}\nCategory: {shop['category']}\nAddress: {shop['address']}"
    self.ids.reviews_list.clear_widgets()

    res = requests.get("http://127.0.0.1:8000/api/reviews/")
    reviews = [r for r in res.json() if r['shop'] == shop['id']]
    for r in reviews:
        self.ids.reviews_list.add_widget(
            OneLineListItem(text=f"★{r['rating']}: {r['comment']}")
        )
class ShopDetailScreen(MDScreen):
    shop_data = {}

    def on_pre_enter(self):
        self.ids.details_label.text = f"""
Name: {self.shop_data['name']}
Category: {self.shop_data['category']}
Address: {self.shop_data['address']}
Phone: {self.shop_data.get('phone_number', 'N/A')}
Website: {self.shop_data.get('website', 'N/A')}
"""
