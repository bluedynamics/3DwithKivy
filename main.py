from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


Builder.load_string("""
<ThreeDeeWithKivyMenu>:
    orientation: 'vertical'
    Button:
        text:'first 3D app'
        on_release: root.start_01()
""")


class ThreeDeeWithKivyMenu(BoxLayout):
    def start_01(self):
        print("start 01")


class ThreeDeeApp(App):
    def build(self):
        return ThreeDeeWithKivyMenu()

if __name__ == '__main__':
    ThreeDeeApp().run()