from time import strftime
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class ClockApp(App):
    pass


if __name__ == '__main__':
    
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name =" Roboto",
                   fn_regular = './Aswsets/Roboto-Regular.ttf',
                   fn_bold = './Aswsets/Roboto-Bold.ttf'
                )
    ClockApp().run()
    
    
    def update_time(self,  nap):
        self.root.ids.time.text = strftime('[b] % H [/b]:  %M : %S')
        
        
def on_start(self):
    ClockApp.schedule_interval(self.update_time, 1)


ClockApp().run()