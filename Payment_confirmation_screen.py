from kivymd.app import MDApp 
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<ButtonBox>:
	orientation:"vertical"
	Widget:
	MDBoxLayout:
		Widget:
		MDIconButton:
			id:button
			size_hint:None, None
			size:"40dp", "40dp"
			icon:""
			icon_size:"40dp"
			theme_text_color:"Custom"
			text_color:[1, 1, 1, 1]
		Widget:
	Widget:
<PayConfirmationScreen>:
	name:"pay_confirmation_screen"
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			heigjt:"60dp"
			md_bg_color:0, 0, 0, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
				orientation:"vertical"
				Widget:
				MDIconButton:
					icon:"arrow-left-bold"
					size_hint:None, None
					size:"50dp", "50dp"
					icon_size:"30dp"
					theme_text_color:"Custom"
					text_color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				MDLabel:
					text:"Confirm Payment"
					text_size:self.size
					font_size:"25dp"
					halign:"center"
					valign:"middle"
					color:1, 1, 1, 1
			MDBoxLayout:
				size_hint_x:None
				width:"50dp"
		MDBoxLayout:
			size_hint_x:None
			width:"300dp"
			orientation:"vertical"
			Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				spacing:5
				Widget:
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				MDBoxLayout:
					size_hint:None, None
					size:"50dp", "50dp"
					md_bg_color:0, 0, 0, 1
					padding:2
					MDBoxLayout:
						md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
						MDLabel:
							text:""
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:1, 1, 1, 1
				Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"300dp"
				ButtonsGrid:
					size_hinth:None, None
					size:"300dp", "300dp"
					cols:3
					rows:4
			Widget:
			MDBoxLayout:
				size_hint_y:None
				height:"50dp"
				padding:"0dp", "10dp"
				ConfirmPaymentButtonBox:
""")
class ButtonBox(MDBoxLayout):
	pass
class ButtonsGrid(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.placeButtons()
	def placeButtons(self):
		for i in range(1,  13):
			button_box = ButtonBox()
			if i == 10:
				button_box.ids.button.icon = "undo-variant"
			elif i == 11:
				button_box.ids.button.icon = "numeric-0-circle"
			elif i == 12:
				button_box.ids.button.icon = "close"
			else:
				button_box.ids.button.icon = "numeric-" + str(i) + "-circle"
			self.add_widget(button_box)