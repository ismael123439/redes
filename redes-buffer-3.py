import random

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.buffer = []

    def enviar_mensaje(self, mensaje, destino):
        # Simular pérdida de paquetes
        if random.random() < 0.2:  # Probabilidad de pérdida de paquete: 20%
            print(f"¡El paquete se perdió en la comunicación desde {self.nombre} hacia {destino.nombre}!")
        else:
            print(f"Mensaje enviado desde {self.nombre} hacia {destino.nombre}: {mensaje}")
            destino.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.buffer.append(mensaje)
        print(f"Mensaje recibido en {self.nombre}: {mensaje}")

    def procesar_buffer(self):
        print(f"Procesando buffer en el nodo {self.nombre}:")
        while self.buffer:
            mensaje = self.buffer.pop(0)  # Eliminar y devolver el primer mensaje en el buffer
            print(f"Mensaje procesado en {self.nombre}: {mensaje}")

# Crear nodos
nodo1 = Nodo("Nodo1")
nodo2 = Nodo("Nodo2")

# Simular comunicación entre nodos
nodo1.enviar_mensaje("Hola Nodo2", nodo2)
nodo2.procesar_buffer()
