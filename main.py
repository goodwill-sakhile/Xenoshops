from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.home import HomeScreen
from screens.shop_list import ShopListScreen
from screens.shop_detail import ShopDetailScreen
from screens.search import SearchScreen

class RetailDirectoryApp(MDApp):
    def build(self):
        self.title = "Retail Shop Directory"
        self.theme_cls.primary_palette = "Blue"
        self.sm = ScreenManager()
        self.load_screens()
        return self.sm

    def load_screens(self):
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(ShopListScreen(name="shop_list"))
        self.sm.add_widget(ShopDetailScreen(name="shop_detail"))
        self.sm.add_widget(SearchScreen(name="search"))

if __name__ == "__main__":
    RetailDirectoryApp().run()
