from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from colores import *
from datos import *

class Boton(App):
    def build(self):
        ### mejorar botones con imagenes
        layout = BoxLayout(orientation='vertical')
        boton1 = Button(text="Actualizar precio", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO,on_press=self.actualizar_precio)
        boton2 = Button(text="Actualizar cantidad", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO,on_press=self.actualizar_cantidad)
        boton3 = Button(text="Consultar precios", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO,on_press=self.consultar_precios)
        boton4 = Button(text="Consultar cantidad", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO,on_press=self.consultar_cantidad)
        boton5 = Button(text="agregar elemento", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO,on_press=self.agregar_elemento)
        layout.add_widget(boton1)
        layout.add_widget(boton2)
        layout.add_widget(boton3)
        layout.add_widget(boton4)
        layout.add_widget(boton5)  
        return layout
        
    def imprimir(self, texto):
        contenido = BoxLayout(orientation="vertical")
        label = Label(text=texto)
        cerrar_boton = Button(text="Cerrar", size_hint=(1, 0.2),background_color=ROSA_NEON)
        contenido.add_widget(label)
        contenido.add_widget(cerrar_boton)
        entrada = Popup(title="resultado", content=contenido, size_hint=(1, 1), size=(400, 200))
        cerrar_boton.bind(on_press=entrada.dismiss)
        entrada.open()
    
    def actualizar_precio(self, instance): 
        pass
        
    def actualizar_cantidad(self, instance):
        pass
        
    def consultar_precios(self, instance):
        pass

    def consultar_cantidad(self, instance):
        pass

    def agregar_elemento(self, instance):
        pass