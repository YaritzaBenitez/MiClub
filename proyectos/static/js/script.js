document.addEventListener('DOMContentLoaded', function() {
    // Agregar evento submit a cada formulario de eliminación
    document.querySelectorAll('.eliminar-formulario').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Evitar el envío del formulario

            // Obtener la acción del formulario
            const action = this.getAttribute('action');

            // Enviar la solicitud POST al endpoint de eliminación
            fetch(action, {
                method: 'POST'
            }).then(response => {
                if (response.ok) {
                    // Si la eliminación es exitosa, redirigir a la página de proyectos
                    window.location.href = '/proyectos';
                } else {
                    // Manejar errores de eliminación
                    console.error('Error al eliminar proyecto:', response.statusText);
                }
            }).catch(error => {
                console.error('Error al eliminar proyecto:', error);
            });
        });
    });

// Función para validar el formulario antes de enviarlo
document.querySelector('form').addEventListener('submit', function(event) {
    // Evitar el envío del formulario
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    var nombre = document.getElementById('nombre').value;
    var descripcion = document.getElementById('descripcion').value;
    var propietario = document.getElementById('propietario').value;
    var fecha_fin_prevista = document.getElementById('fecha_fin_prevista').value;
    var fecha_fin_real = document.getElementById('fecha_fin_real').value;


    // Verificar si algún campo está vacío
    if (!nombre || !descripcion || !propietario || !fecha_fin_prevista || !fecha_fin_real) {
        // Mostrar el mensaje de advertencia
        document.getElementById('mensaje-incompleto').style.display = 'block';
        return; // Detener el envío del formulario
    }

    // Si todos los campos están completos, ocultar el mensaje de advertencia
    document.getElementById('mensaje-incompleto').style.display = 'none';

    // Enviar el formulario si todos los campos están completos
    this.submit();
});

});