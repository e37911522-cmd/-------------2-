from kivy.app import App
from kivy.label import Label


class PomogatorApp(App):

    def build(self):
        return Label(text='Привет, это Помогатор 3 тысячи!')


if __name__ == '__main__':
    PomogatorApp().run()