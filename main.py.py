from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols =1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5 }
        #add widgets to window


        self.window.add_widget(Image(source="logo.png"))
        self.greeting = Label(
                            text="what s your name?",
                            font_size = 40,
                            color='288783'                              
                              )
        self.window.add_widget(self.greeting )
        self.user = TextInput(
            multiline=False,
            padding_y = (20,20),
            size_hint =(1, 0.5)
            
            )
        self.window.add_widget(self.user)
        self.button = Button(
            text="Greet",
            size_hint =(1,0.5),
            bold =True,
            background_color = '288783',
            background_normal =""
            )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        
        return self.window
    


    def callback(self, instancs):
        self.greeting.text ="hello " + self.user.text + "!"

       

if __name__ == "__main__":
    SayHello().run()

