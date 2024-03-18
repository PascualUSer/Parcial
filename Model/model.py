from enum import Enum

class EstadoTarea(Enum):
    PENDIENTE = 1
    COMPLETADA = 2

class Tarea:
    def __init__(self, id, titulo, descripcion, fecha_vencimiento, estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.etiquetas = []  # Lista de etiquetas asociadas a la tarea

    def agregar_etiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)

    def eliminar_etiqueta(self, etiqueta):
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)
