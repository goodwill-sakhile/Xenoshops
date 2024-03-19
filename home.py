from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
root = Builder.load_string("""
<RoundShopIcon>:
	size_hint:None, None
	size:"70dp", "70dp" 
	md_bg_color:1, 1, 1, 1
	radius:70, 70, 70, 70
	Widget:
	MDBoxLayout:
		md_bg_color:0, 0, 0, 1
		size_hint:None, None
		size:"65dp", "65dp"
		radius:65, 65, 65, 65
		pos_hint:{"center_x":.5, "center_y":.5}
	Widget:
<HomeScreen>:
	name:"home_screen"
	MDBoxLayout:
		md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
		MDBoxLayout:
			orientation:"vertical"
			padding:5
			MDBoxLayout:
				size_hint_y:None
				height:"60dp"
				md_bg_color:0, 0, 0, 1
				MDBoxLayout:
					size_hint_x:None
					width:"50dp"
					orientation:"vertical"
					Widget:
					MDIconButton:
						size_hint:None, None
						size:"40dp", "40dp" 
						icon:"logout"
						icon_size:"30dp"
						theme_text_color:"Custom"
						pos_hint:{"center_x":.5, "center_y":.5}
						text_color:1, 1, 1, 1
				MDBoxLayout:
					MDLabel:
						text:"Xenoshops"
						text_size:self.size
						halign:"center"
						valign:"middle"
						font_size:"18dp"
						color:1, 1, 1, 1
				MDBoxLayout:
					size_hint_x:None
					width:"50dp"
					orientation:"vertical"
					Widget:
					MDIconButton:
						size_hint:None, None
						size:"40dp", "40dp"
						icon:"cart-arrow-down"
						icon_size:"30dp"
						theme_text_color:"Custom"
						text_color:1, 1, 1, 1
						pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
				Widget: 
				MDBoxLayout:
					size_hint_x:None
					width:"300dp" 
					orientation:"vertical"
					MDBoxLayout:
						size_hint_y:None
						height:"100dp"
						ScrollView:
							size_hint:None, None
							size:self.parent.size
							bar_width:0
							ShopsLayout:
					MDBoxLayout: 
						orientation:"vertical"
						Widget:
						MDBoxLayout:
							size_hint_y:None
							height:"400dp"
							md_bg_color:0, 1, 1, 1
							orientation:"vertical"
							spacing:5
							MDBoxLayout:
								spacing:5
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
							MDBoxLayout:
								spacing:5
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
							MDBoxLayout:
								spacing:5
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
								MDBoxLayout:
									md_bg_color:0, 0, 0, 1
						Widget:
				Widget:
""")
class RoundShopIcon(MDBoxLayout):
	pass
class ShopsLayout(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.size_hint_x = None
		self.rows = 1
		self.spacing = "10dp"
		self.padding = "10dp", "15dp"
		self.bind(minimum_width = self.setter("width"))
		self.ListShops()
	def ListShops(self):
		for i in range(5):
			shop = RoundShopIcon()
			self.add_widget(shop)
class HomeScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = HomeScreen()
		return root
if __name__ == "__main__":
	TestApp().run()