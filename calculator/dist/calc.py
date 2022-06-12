from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
import sys
import os

Builder.load_string("""

#: import  utils kivy.utils
<Root>

    BoxLayout:
        orientation: "vertical"
        size: root.width,root.height

        TextInput:
            id: score
            text: "0"
            halign : "right"
            font_size: 65
            size_hint: (1, .15)
            multiline: False


        GridLayout:
            size: root.width,root.height
            cols: 4
            rows: 5

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "CE"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.clear()
            Button:
                id: clear
                size_hint: (0.2,0.2)
                font_size: 32
                text: "C"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.clear()

            Button:

                size_hint: (0.2,0.2)
                font_size: 32
                text: u"\u00AB"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.remove()

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "/"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.divide_sign()

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "7"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(7)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "8"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(8)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "9"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(9)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "X"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.multiply_sign()


            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "4"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(4)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "5"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(5)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "6"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(6)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "-"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.subtract_sign()


            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "1"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(1)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "2"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(2)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "3"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(3)

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "+"
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.add_sign()

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "+/-"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.pos_neg()

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "0"
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.button_press(0)
            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "."
                color: utils.get_color_from_hex('03fc84')
                background_normal:''
                background_color: utils.get_color_from_hex('000000')
                on_press: root.dot()

            Button:
                size_hint: (0.2,0.2)
                font_size: 32
                text: "="
                color: utils.get_color_from_hex('000000')
                background_normal:''
                background_color: utils.get_color_from_hex('03fc84')
                on_press: root.equals()

""")
# Window.size = (450, 600)

class Root(Widget):
    def clear(self):
        self.ids.score.text = "0"
        self.ids.score.color = "000000"


    def button_press(self, button):
        prior = self.ids.score.text
        if "Error" in prior:
            prior = ''
        elif prior == "0":
            self.ids.score.text = ''
            self.ids.score.text = f'{button}'
        else:
            self.ids.score.text = f'{prior}{button}'


    def add_sign(self):
        prior = self.ids.score.text
        if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
            pass
        else:
            self.ids.score.text = f"{prior}+"



    def subtract_sign(self):
        prior = self.ids.score.text
        if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
            pass
        else:
            self.ids.score.text = f"{prior}-"

    def multiply_sign(self):

        prior = self.ids.score.text
        if prior[-1] == "/" or prior[-1] == "+"  or prior[-1] == "-" or prior == "**" :
            pass
        elif "**"  in prior:
            pass
        else:
            self.ids.score.text = f"{prior}*"


    def divide_sign(self):
        prior = self.ids.score.text
        if prior[-1] == "-" or prior[-1] == "+"  or prior[-1] == "/" or prior[-1] == "*":
            pass
        else:
            self.ids.score.text = f"{prior}/"

    def dot(self):
        prior = self.ids.score.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.score.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.score.text = prior



    def equals(self):

        try :

            allowed = ["0","1","2","3","4","5","6","7","8","9","+","-","/","*","%","."]

            prior = self.ids.score.text
            prior = list(prior)
            for i in prior:
                if i not in allowed:
                    self.ids.score.text = "0"
                else:
                    answer = eval(self.ids.score.text)
                    self.ids.score.text = str(answer)
        except:
            self.ids.score.text = "Eroor"

    def remove(self):
        prior = self.ids.score.text
        prior = prior[:-1]
        self.ids.score.text = prior


    def pos_neg(self):
        prior = self.ids.score.text
        if "-" in prior[0]:
            self.ids.score.text = f'{prior.replace("-","")}'
        else:
            self.ids.score.text = f'-{prior}'

class CalcApp(App):
    def build(self):
        self.icon = "icon.png"
        return Root()



if __name__ == '__main__':
    CalcApp().run()