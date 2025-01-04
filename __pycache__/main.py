from kivy.app import App #importa a classe app responsavel por definir como uma apliçâo movel
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout #Layout organiza

from instructions import txt_instruction, txt_test1

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text = txt_instruction)
        
        lbl1 = Label(text='Enter your name', halign='right')
        self.in_name = TextInput(multiline=False)
        
        lbl2 = Label(text='Enter your age', halign='right')
        self.in_age = TextInput(multiline=False)
        
        self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5})#center_x representa a posicçao horizontal central do widget de 0 borda esquerda a 1 borda direita
        
        line1 = BoxLayout(size_hint=(0.8,None), height = '30sp') #scalated_individual pixels
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        
        line2 = BoxLayout(size_hint=(0.8,None), height = '30sp') 
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        
        self.add_widget(outer)

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        instr = Label(text=txt_test1)
        lbl_result = Label(text='Enter the result', halign = 'right')
        self.in_result = TextInput(text='0', multiline = False) #multiline false signuifica uma linha unica na input
        self.btn = Button(text='Next', size_hint = (0.3, 0.2), pos_hint={'center_x':0.5})
        
        line = BoxLayout(size_hint=(0.8,None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        
        self.add_widget(outer)
        

        
    
class Checksits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

class Heartcheck(App):
    def build(self): #build é o metodo para renderização grafica em kivy
        return PulseScr()
    

Heartcheck().run()#run é o loop onde acontece a aplicação