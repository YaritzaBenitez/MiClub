# Importaciones necesarias para el funcionamiento de Flask y otras utilidades
from flask import Flask, render_template, request, redirect, url_for

# Definición de la clase base Proyecto
class Proyecto:
    def __init__(self, nombre, descripcion, propietario, fecha_fin_prevista, fecha_inicio=None, fecha_fin_real=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.propietario = propietario
        self.fecha_fin_prevista = fecha_fin_prevista
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_real = fecha_fin_real

    def __str__(self):
        return f"{self.nombre} - Propietario: {self.propietario}"


# Definición de la subclase ProyectoSoftware que hereda de Proyecto
class ProyectoSoftware(Proyecto):
    def __init__(self, nombre, descripcion, propietario, fecha_fin_prevista, lenguaje):
        super().__init__(nombre, descripcion, propietario, fecha_fin_prevista)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"{super().__str__()} - Lenguaje: {self.lenguaje}"

# Clase principal que gestiona la aplicación Flask
class ProyectosApp:
    def __init__(self):
        # Inicialización de la aplicación Flask
        self.app = Flask(__name__, template_folder='D:/Lib/site-packages/flask/proyectos/templates', static_folder='D:/Lib/site-packages/flask/proyectos/static')
        # Lista para almacenar los proyectos guardados
        self.proyectos_guardados = []

        # Definición de las reglas de enrutamiento
        self.app.add_url_rule('/', view_func=self.index)
        self.app.add_url_rule('/proyectos', view_func=self.ver_proyectos)
        self.app.add_url_rule('/guardar_proyecto', view_func=self.guardar_proyecto, methods=['POST'])
        self.app.add_url_rule('/proyecto/<int:id>', view_func=self.ver_proyecto)
        self.app.add_url_rule('/eliminar_proyecto/<nombre>', view_func=self.eliminar_proyecto, methods=['POST'])  # Cambiado el parámetro a nombre

    # Vista para la página de inicio
    def index(self):
        return render_template('index.html')

    # Vista para mostrar todos los proyectos guardados
    def ver_proyectos(self):
        return render_template('proyectos.html', proyectos=self.proyectos_guardados)

    def guardar_proyecto(self):
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            descripcion = request.form.get('descripcion')
            propietario = request.form.get('propietario')
            fecha_inicio = request.form.get('fecha_inicio')
            fecha_fin_prevista = request.form.get('fecha_fin_prevista')
            fecha_fin_real = request.form.get('fecha_fin_real')
            proyecto = Proyecto(nombre, descripcion, propietario, fecha_fin_prevista, fecha_inicio, fecha_fin_real)
            self.proyectos_guardados.append(proyecto)
            return redirect(url_for('ver_proyectos'))  # Redireccionamiento a la página de visualización de proyectos
        return redirect(url_for('index')) 


    # Vista para mostrar los detalles de un proyecto específico
    def ver_proyecto(self, id):
        if id < len(self.proyectos_guardados):
            proyecto = self.proyectos_guardados[id]
            return render_template('ver_proyecto.html', proyecto=proyecto)
        else:
            return "Proyecto no encontrado"
            

    def eliminar_proyecto(self, nombre):
        if request.method == 'POST':
            # Obtener el ID del recuadro desde el cuerpo de la solicitud
            recuadro_id = request.json.get('id')
            
            # Buscar el proyecto por ID y eliminarlo si se encuentra
            proyecto = next((p for p in self.proyectos_guardados if p.nombre == recuadro_id), None)
            if proyecto:
                self.proyectos_guardados.remove(proyecto)
                return redirect(url_for('ver_proyectos'))
            else:
                return "Proyecto no encontrado"
        return redirect(url_for('index'))

    
    


    # Método para iniciar el servidor Flask
    def run(self):
        self.app.run(debug=True)

# Entrada principal del programa
if __name__ == "__main__":
    app = ProyectosApp()
    app.run()  # Inicia la aplicación Flask
