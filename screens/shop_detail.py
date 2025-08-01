from kivymd.uix.screen import MDScreen

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
