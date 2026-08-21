class SerpientesVenenosas:
    def __init__(self, nombre, veneno):
        self.nombre = nombre
        self.veneno = veneno

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("¿Es venenosa?:", self.veneno)


equis = SerpientesVenenosas("equis", "boa")
boa = SerpientesVenenosas("boa", "no venenosa")

equis.mostrar_informacion()
boa.mostrar_informacion()