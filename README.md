# Proyecto-AS
Descripción
Este proyecto es una plataforma de gestión comunitaria que permite a los residentes, conserjes y administradores de comunidades interactuar entre sí, participar en foros y subforos, gestionar reservas de espacios comunes y recibir notificaciones importantes sobre la comunidad.

Configuración del Entorno de Desarrollo
1. Clonar el Repositorio
* git clone https://github.com/Sp1ike/Proyecto-AS.git
* cd Proyecto-AS

2. Instalar Dependencias
Asegúrate de tener Python y pip instalados. Luego, crea y activa un entorno virtual e instala las dependencias del proyecto:
* python -m venv venv
* source venv/bin/activate (para sistemas basados en Unix)
* venv\Scripts\activate (para Windows)
* pip install -r requirements.txt

3. Configurar la Aplicación
Copiar el archivo de configuración de ejemplo y modificarlo según sea necesario:
* cp config.py.example config.py

4. Iniciar la Aplicación
* flask run

Uso de la API
Endpoints Disponibles
* /comunidades: Obtener todas las comunidades.
* /comunidades/<id_comunidad>: Obtener detalles de una comunidad específica.
* /foros: Obtener todos los foros.
* /foros/<id_foro>: Obtener detalles de un foro específico.
Para obtener información sobre otros endpoints y parámetros, consulta la documentación de la API en el archivo API_DOCUMENTATION.md.

Contribución
Si deseas contribuir al proyecto, sigue estos pasos:
1. Realiza un fork del repositorio.
2. Crea una nueva rama: git checkout -b feature/nueva-funcionalidad
3. Realiza tus cambios y haz commits: git commit -am 'Añadir nueva funcionalidad'
4. Sube tus cambios a tu fork: git push origin feature/nueva-funcionalidad
5. Envía una solicitud de extracción a la rama principal del repositorio original.
