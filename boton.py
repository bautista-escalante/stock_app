from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from datos import *
from colores import *

class Boton(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        boton1 = Button(text="Actualizar precio", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO)
        boton1.bind(on_press=self.actualizar_precio)
        
        boton2 = Button(text="Actualizar cantidad", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO)
        boton2.bind(on_press=self.actualizar_cantidad)
        
        boton3 = Button(text="Consultar precios", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO)
        boton3.bind(on_press=self.consultar_precios)
        
        boton4 = Button(text="Consultar cantidad", size_hint=(1, 0.1),color=DORADO,background_color=ROSA_INTENSO)
        boton4.bind(on_press=self.consultar_precios)
        
        layout.add_widget(boton1)
        layout.add_widget(boton2)
        layout.add_widget(boton3)
        layout.add_widget(boton4)
        
        return layout
    
    def actualizar_precio(self, instance):
        print("Botón 'Actualizar precio' presionado.")
        actualizar_precios("mobiliario",0.05)
        
    def actualizar_cantidad(self, instance):
        print("Botón 'Actualizar cantidad' presionado.")
        
    def consultar_precios(self, instance):
        print("Botón 'Consultar precios' presionado.")

    def consultar_precios(self, instance):
        print("Botón 'Consultar cantidad' presionado.")
        lista=mostrar_categoria("mobiliario")
        print("cantidad  categoria  nombre  alquiler  reposicion ")
        for datos in lista:
            print(f"{datos[1]}     {datos[2]}   {datos[3]}   {datos[4]}    {datos[5]}")




