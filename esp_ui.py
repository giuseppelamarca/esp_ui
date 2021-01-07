# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class Esp_ui(FloatLayout):
    def __init__(self, **kwargs):
        super(Esp_ui, self).__init__(**kwargs)
        self.pin_ = list()
        self.pin_mode_ = list()

    def pin(self, text):
        if text not in self.pin_:
            self.pin_.append(text)

    def pin_mode(self, text):
        if text not in self.pin_mode_:
            self.pin_mode_.append(text)

    def generate(self):
        print("generate")
        print(list(zip(self.pin_, self.pin_mode_)))


class Esp_uiApp(App):
    def build(self):
        return Esp_ui()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Esp_uiApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
