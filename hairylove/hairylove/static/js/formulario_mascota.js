/**
 * Script para manejar el formulario dinámico de registro de mascotas
 * Carga razas dinámicamente según la especie seleccionada
 * Maneja géneros y tamaños con opciones predefinidas
 */

document.addEventListener('DOMContentLoaded', function() {
    // Obtener referencias a los elementos del DOM
    const especieSelect = document.getElementById('id_Especie');
    const razaSelect = document.getElementById('id_Raza');
    const generoSelect = document.getElementById('id_Genero');
    const tamanioSelect = document.getElementById('id_Tamaño');

    // Verificar que los elementos existan
    if (!especieSelect || !razaSelect) {
        console.warn('Los elementos del formulario no fueron encontrados');
        return;
    }

    // Cargar géneros al iniciar
    cargarGeneros();
    
    // Cargar tamaños al iniciar
    cargarTamanos();

    // Evento para cambio de especie
    especieSelect.addEventListener('change', function() {
        const especie = this.value;
        if (especie) {
            cargarRazas(especie);
        } else {
            // Limpiar razas si se deselecciona especie
            razaSelect.innerHTML = '<option value="">---------</option>';
        }
    });

    /**
     * Carga las razas desde la API según la especie seleccionada
     */
    function cargarRazas(especie) {
        // Mostrar loading
        razaSelect.innerHTML = '<option value="">Cargando razas...</option>';
        razaSelect.disabled = true;

        fetch(`/adopcion/api/razas-por-especie/?especie=${encodeURIComponent(especie)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la respuesta de la API');
                }
                return response.json();
            })
            .then(data => {
                // Limpiar opciones previas
                razaSelect.innerHTML = '<option value="">---------</option>';

                // Agregar nuevas opciones
                if (data.razas && data.razas.length > 0) {
                    data.razas.forEach(raza => {
                        const option = document.createElement('option');
                        option.value = raza;
                        option.textContent = raza;
                        razaSelect.appendChild(option);
                    });
                    razaSelect.disabled = false;
                } else {
                    console.warn('No se encontraron razas para esta especie');
                    razaSelect.disabled = false;
                }
            })
            .catch(error => {
                console.error('Error al cargar razas:', error);
                razaSelect.innerHTML = '<option value="">Error al cargar razas</option>';
                razaSelect.disabled = false;
            });
    }

    /**
     * Carga los géneros disponibles desde la API
     */
    function cargarGeneros() {
        if (!generoSelect) return;

        fetch('/adopcion/api/generos/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la respuesta de la API');
                }
                return response.json();
            })
            .then(data => {
                // Limpiar opciones previas
                generoSelect.innerHTML = '<option value="">---------</option>';

                // Agregar nuevas opciones
                if (data.generos && data.generos.length > 0) {
                    data.generos.forEach(genero => {
                        const option = document.createElement('option');
                        option.value = genero.value;
                        option.textContent = genero.label;
                        generoSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('Error al cargar géneros:', error);
            });
    }

    /**
     * Carga los tamaños disponibles desde la API
     */
    function cargarTamanos() {
        if (!tamanioSelect) return;

        fetch('/adopcion/api/tamanos/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la respuesta de la API');
                }
                return response.json();
            })
            .then(data => {
                // Limpiar opciones previas
                tamanioSelect.innerHTML = '<option value="">---------</option>';

                // Agregar nuevas opciones
                if (data.tamanos && data.tamanos.length > 0) {
                    data.tamanos.forEach(tamano => {
                        const option = document.createElement('option');
                        option.value = tamano.value;
                        option.textContent = tamano.label;
                        tamanioSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('Error al cargar tamaños:', error);
            });
    }

    /**
     * Si la página se carga con una especie ya seleccionada, cargar sus razas
     */
    if (especieSelect.value) {
        cargarRazas(especieSelect.value);
    }
});
