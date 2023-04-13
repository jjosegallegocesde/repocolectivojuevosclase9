class Juan_Pablo:
    def __init__(self):
        self.nombre = "Juan Pablo"
        self.apellido = "Jaramillo"
        self.edad = 27
        self.mascotas = True
        self.tatuajes = True
        
    def saludar (self):
        return (f"Hola soy un {self.nombre}")   
    
    
nombre_uno = Juan_Pablo()

resultado = nombre_uno.saludar()    
    
print(resultado)
    
