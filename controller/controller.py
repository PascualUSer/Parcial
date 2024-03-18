from Model.model import Tarea
from view.view import PantallaPrincipal

class ControladorTareas:
    def __init__(self):
        self.tareas = []
        self.pantalla_principal = PantallaPrincipal()

    def crear_tarea(self, titulo, descripcion, fecha_vencimiento, estado, etiquetas):
        id = len(self.tareas) + 1 
        tarea = Tarea(id, titulo, descripcion, fecha_vencimiento, estado)
        for etiqueta in etiquetas:
            tarea.agregar_etiqueta(etiqueta.strip())
        self.tareas.append(tarea)
        self.pantalla_principal.mostrar_mensaje("Tarea creada exitosamente.")

    def editar_tarea(self, id, titulo, descripcion, fecha_vencimiento, estado, etiquetas):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.titulo = titulo
                tarea.descripcion = descripcion
                tarea.fecha_vencimiento = fecha_vencimiento
                tarea.estado = estado
                tarea.etiquetas = etiquetas
                self.pantalla_principal.mostrar_exito_editar()
                return
        self.pantalla_principal.mostrar_mensaje("No se encontró la tarea para editar.")

    def eliminar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                self.tareas.remove(tarea)
                self.pantalla_principal.mostrar_exito_eliminar()
                return
        self.pantalla_principal.mostrar_mensaje("No se encontró la tarea para eliminar.")

    def ejecutar(self):
        while True:
            opcion = input("1. Crear tarea\n2. Ver tareas\n3. Editar tarea\n4. Eliminar tarea\n5. Salir\nSeleccione una opción: ")

            if opcion == "1":
                titulo, descripcion, fecha_vencimiento, estado, etiquetas = self.pantalla_principal.solicitar_datos()
                self.crear_tarea(titulo, descripcion, fecha_vencimiento, estado, etiquetas)
            elif opcion == "2":
                self.pantalla_principal.mostrar(self.tareas)
            elif opcion == "3":
                id = self.pantalla_principal.solicitar_id_tarea_editar()
                titulo, descripcion, fecha_vencimiento, estado, etiquetas = self.pantalla_principal.solicitar_datos()
                self.editar_tarea(id, titulo, descripcion, fecha_vencimiento, estado, etiquetas)
            elif opcion == "4":
                id = self.pantalla_principal.solicitar_id_tarea_eliminar()
                self.eliminar_tarea(id)
            elif opcion == "5":
                break
            else:
                self.pantalla_principal.mostrar_mensaje("Opción no válida. Por favor, seleccione nuevamente.")
