from kivymd.app import MDApp 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<HomeScreen>:
	name:"home_screen"
	MDBoxLayout:
		md_bg_color:0, 0, 0, 1
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"logout"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
			MDBoxLayout:
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				MDIconButton:
					size_hint:None, None
					size:"50dp", "50dp"
					icon:"cart"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
					pos_hint:{"center_x":.5, "center_y":.5}
		MDBoxLayout:
			radius:20, 20, 0, 0
			md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
			Widget:
			MDBoxLayout:
				size_hint_x:None
				width:"300dp"
			Widget:
""")
class HomeScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = HomeScreen()
		return root
if __name__ == "__main__":
	TestApp().run()