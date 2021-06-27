from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

class HandsFreeCallingApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jsonFile = JsonStore("user_info.json")


    def build(self):
        Window.maximize()
        self.title = "Hands Free App"
        return Builder.load_file("hands_free.kv")

    # noinspection PyBroadException
    def on_start(self):
        try:
            if self.jsonFile.get("UserInfo")["user_pin"] != "":
                self.root.current = "SCRN_Main"
                name = self.jsonFile.get("UserInfo")["full_name"].split()
                self.root.get_screen("SCRN_Main").ids.user_greeting.text = f'[color=DAA520]Welcome,[/color] [color=C0C0C0]{name[0]}[/color]'
        except Exception:
            pass

    def continue_to_main(self) -> None:
        self.jsonFile.put(
            "UserInfo",
            full_name=self.root.get_screen("SCRN_Setup").ids.full_name.text,
            user_pin=self.root.get_screen("SCRN_Setup").ids.user_pin.text
        )
        self.root.current = "SCRN_Main"
        first_name = self.root.get_screen("SCRN_Setup").ids.full_name.text.split()
        self.root.get_screen("SCRN_Main").ids.user_greeting.text = f'[color=DAA520]Welcome,[/color] [color=C0C0C0]{first_name[0]}[/color]'

HandsFreeCallingApp().run()