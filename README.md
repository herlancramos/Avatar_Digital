Requisitos Previos
Asegúrate de tener instalado lo siguiente antes de empezar:

Python 3.x – para ejecutar el script de extracción.

OpenCV – biblioteca de visión artificial.

XAMPP – para levantar un servidor local con Apache.

Instala la dependencia de Python con:

pip install opencv-python

Fase 1: Extracción de Fotogramas (Python)
El script extraer.py lee el video y guarda imágenes cada cierto número de fotogramas, listas para ser usadas en software de fotogrametría (Meshroom, RealityCapture, etc.).

Instrucciones:
Coloca tu video
Copia tu archivo .mp4 dentro de la carpeta VIDEO_PARA_EL_3D/video/.

Ejecuta el script
Abre una terminal (cmd, PowerShell o bash) y navega hasta la carpeta del script:

cd "ruta\completa\VIDEO_PARA_EL_3D"
python extraer.py

Resultado
Las imágenes se guardarán automáticamente en VIDEO_PARA_EL_3D/fotos/ con nombres como foto_0000.jpg, foto_0001.jpg, etc.

Fase 2: Despliegue en Servidor Local (XAMPP)
Una vez que hayas procesado las imágenes con tu software de fotogrametría y obtenido el modelo 3D (archivos .obj, .gltf, texturas, etc.), debes montar el visualizador web.

Pasos:
Copia la carpeta avatar3d (la que contiene index.html y tus archivos 3D) dentro del directorio raíz de XAMPP:

C:\xampp\htdocs\avatar3d\

Enciende Apache
Abre el Panel de Control de XAMPP y haz clic en Start junto a Apache. Debe ponerse en verde.

Fase 3: Visualización en el Navegador
Abre tu navegador favorito (Chrome, Edge, Firefox) y escribe la siguiente dirección:

http://localhost/avatar3d/

Si todo está correcto, verás el visualizador interactivo de tu avatar 3D. Podrás:

Rotar la cámara con el mouse.

Hacer zoom con la rueda del ratón.

Examinar la textura y geometría generadas por fotogrametría.

Notas adicionales
El script extraer.py asume que dentro de video/ hay un solo archivo .mp4. Si hay más de uno, modifica el código para elegir el deseado.

Puedes usar cualquier software de fotogrametría. Yo personalmente usé Meshroom (gratuito y open source).

Asegúrate de que los archivos 3D exportados estén referenciados correctamente en index.html. Por ejemplo, si usas Three.js, verifica la ruta del modelo.

Si el visualizador no carga, abre la consola del navegador (F12) para ver posibles errores de rutas o CORS (con XAMPP esto no debería ocurrir).
