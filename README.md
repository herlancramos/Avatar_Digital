# Estructura del Proyecto
Avatar Digital/
│
├── VIDEO_PARA_EL_3D/               #  Módulo de procesamiento de video
│   ├── video/                      #  Coloca aquí tu archivo .mp4
│   ├── fotos/                      #  Aquí se guardarán los fotogramas extraídos
│   └── extraer.py                  #  Script de extracción de fotogramas
│
├── avatar3d/                       #  Módulo web (visualizador 3D)
│   ├── index.html                  #  Página principal
│   └── [archivos del modelo 3D]    #  Objeto 3D, texturas, librerías WebGL
│
└── README.md                       #  Este archivo
⚙️ Requisitos Previos
Asegúrate de tener instalado lo siguiente antes de empezar:

Python 3.x – para ejecutar el script de extracción.

OpenCV – biblioteca de visión artificial.

XAMPP – para levantar un servidor local con Apache.

Instala la dependencia de Python con:

bash
pip install opencv-python
🚀 Fase 1: Extracción de Fotogramas (Python)
El script extraer.py lee el video y guarda imágenes cada cierto número de fotogramas, listas para ser usadas en software de fotogrametría (Meshroom, RealityCapture, etc.).

Instrucciones:
Coloca tu video
Copia tu archivo .mp4 dentro de la carpeta VIDEO_PARA_EL_3D/video/.

Ejecuta el script
Abre una terminal (cmd, PowerShell o bash) y navega hasta la carpeta del script:

bash
cd "ruta\completa\VIDEO_PARA_EL_3D"
python extraer.py
Resultado
Las imágenes se guardarán automáticamente en VIDEO_PARA_EL_3D/fotos/ con nombres como foto_0000.jpg, foto_0001.jpg, etc.

Personalización:
Edita el archivo extraer.py y modifica los siguientes parámetros:

python
# Cambia el número 8 por la frecuencia que desees (ej: 1, 5, 10, etc.)
extraer_fotogramas(video_path, output_folder, cada_n_frames=8)

# También puedes ajustar la calidad JPEG (95 es un buen valor)
cv2.imwrite(ruta_imagen, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
cada_n_frames : número de fotogramas que se saltan entre cada extracción. Un valor más bajo da más imágenes (mayor detalle, pero más pesado).

calidad : entre 0 y 100. 95 preserva muy bien los detalles para fotogrametría.

🌐 Fase 2: Despliegue en Servidor Local (XAMPP)
Una vez que hayas procesado las imágenes con tu software de fotogrametría y obtenido el modelo 3D (archivos .obj, .gltf, texturas, etc.), debes montar el visualizador web.

Pasos:
Copia la carpeta avatar3d (la que contiene index.html y tus archivos 3D) dentro del directorio raíz de XAMPP:

text
C:\xampp\htdocs\avatar3d\
Enciende Apache
Abre el Panel de Control de XAMPP y haz clic en Start junto a Apache. Debe ponerse en verde.

💻 Fase 3: Visualización en el Navegador
Abre tu navegador favorito (Chrome, Edge, Firefox) y escribe la siguiente dirección:

text
http://localhost/avatar3d/
Si todo está correcto, verás el visualizador interactivo de tu avatar 3D. Podrás:

Rotar la cámara con el mouse.

Hacer zoom con la rueda del ratón.

Examinar la textura y geometría generadas por fotogrametría.

🧠 Notas adicionales
El script extraer.py asume que dentro de video/ hay un solo archivo .mp4. Si hay más de uno, modifica el código para elegir el deseado.

Puedes usar cualquier software de fotogrametría. Yo personalmente usé Meshroom (gratuito y open source).

Asegúrate de que los archivos 3D exportados estén referenciados correctamente en index.html. Por ejemplo, si usas Three.js, verifica la ruta del modelo.

Si el visualizador no carga, abre la consola del navegador (F12) para ver posibles errores de rutas o CORS (con XAMPP esto no debería ocurrir).
