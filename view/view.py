from Model.model import EstadoTarea

class InterfazUsuario:
    def mostrar_tareas(self, tareas):
        print("Tareas:")
        for tarea in tareas:
            print(f"ID: {tarea.id}, Título: {tarea.titulo}, Descripción: {tarea.descripcion}, "
                  f"Fecha de vencimiento: {tarea.fecha_vencimiento}, Estado: {tarea.estado.name}, "
                  f"Etiquetas: {', '.join(tarea.etiquetas)}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def solicitar_datos(self):
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
        estado = EstadoTarea.PENDIENTE  
        etiquetas = input("Ingrese etiquetas separadas por comas (opcional): ").split(',')
        return titulo, descripcion, fecha_vencimiento, estado, etiquetas

    def solicitar_id_tarea_editar(self):
        return int(input("Ingrese el ID de la tarea a editar: "))

    def solicitar_id_tarea_eliminar(self):
        return int(input("Ingrese el ID de la tarea a eliminar: "))


class PantallaPrincipal:
    def __init__(self):
        self.interfaz_usuario = InterfazUsuario()

    def mostrar(self, tareas):
        self.interfaz_usuario.mostrar_tareas(tareas)

    def mostrar_mensaje(self, mensaje):
        self.interfaz_usuario.mostrar_mensaje(mensaje)

    def solicitar_datos(self):
        return self.interfaz_usuario.solicitar_datos()

    def solicitar_id_tarea_editar(self):
        return self.interfaz_usuario.solicitar_id_tarea_editar()

    def solicitar_id_tarea_eliminar(self):
        return self.interfaz_usuario.solicitar_id_tarea_eliminar()

    def mostrar_exito_editar(self):
        self.interfaz_usuario.mostrar_mensaje("Tarea editada exitosamente.")

    def mostrar_exito_eliminar(self):
        self.interfaz_usuario.mostrar_mensaje("Tarea eliminada exitosamente.")
