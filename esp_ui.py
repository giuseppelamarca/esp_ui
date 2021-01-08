# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

OUTPUT = 'GPIO_MODE_OUTPUT'
INPUT = 'GPIO_MODE_INPUT'
POSITIVE_INT = 'GPIO_INTR_POSEDGE'
NEGATIVE_INT = 'GPIO_INTR_NEGEDGE'
ANY_INT = 'GPIO_INTR_ANYEDGE'

modes = [OUTPUT, INPUT, POSITIVE_INT ,NEGATIVE_INT, ANY_INT]

class Esp_ui(FloatLayout):
    def __init__(self, **kwargs):
        super(Esp_ui, self).__init__(**kwargs)
        self.pin_ = [''] * 16
        self.pin_mode_ = [''] * 16
        self.ident_level = 0            #updated by different functions for correct identation
        self.config_exist = False

    def tab(self):
        return str(self.ident_level * ' ' * 8)

    def pin(self, pin, text):
        if text not in self.pin_:
            self.pin_[pin - 1] = text

    def pin_mode(self, pin, text):
        self.pin_mode_[pin - 1] = text

    def generate(self):
        print("generate")
        self.config = dict(zip(self.pin_, self.pin_mode_))
        print(self.config)
        self.create_file()
        self.create_main()
        for mode in set(self.pin_mode_):
            self.pin_config(mode)
        self.close_main()

    def create_file(self):
        self.file = open('main.c', 'w')

    def create_main(self):
        self.file.write("void app_main()\n{")

    def pin_config(self, mode):
        self.ident_level += 1
        if self.config_exist:
            self.file.write(self.tab() + "conf = {\n")
        else:
            self.file.write(self.tab() + "gpio_config_t conf = {\n")
        self.ident_level += 1
        self.file.write(self.tab() + ".pull_down_en = 0, \n")
        self.file.write(self.tab() + ".pull_down_en = 0, \n")
        self.file.write(self.tab() + ".pull_up_en = 0, \n")
        if mode == INPUT or mode == OUTPUT:
            self.file.write(self.tab() + ".intr_type = GPIO_INTR_DISABLE, \n")
            self.file.write(self.tab() + ".mode = " + mode + ", \n")

        else:
            self.file.write(self.tab() + ".intr_type = " +mode +" ,\n")
            self.file.write(self.tab() + ".mode = " + INPUT + ", \n")

        bit_mask = ''
        for pin_, mode_ in self.config.items():
            if pin_ == '' or mode_ == '':
                continue
            if mode_ == mode:
                if bit_mask == '':
                    pass
                else:
                    bit_mask += " | "
                bit_mask += "(1ULL<<" + pin_ + ") "

        self.file.write(self.tab() + ".pin_bit_mask = " + bit_mask + ", \n")

        self.ident_level -= 1
        self.file.write(self.tab() + "};\n")
        self.file.write(self.tab()+ "gpio_config(&conf);\n")
        self.ident_level -= 1
        self.config_exist = True


    def close_main(self):
        self.file.write('}')
        self.file.close()

class Esp_uiApp(App):
    def build(self):
        return Esp_ui()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Esp_uiApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
