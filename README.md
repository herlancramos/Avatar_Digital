# VIDEO_PARA_EL_3D

# Requisitos Previos

Asegúrate de tener instalado lo siguiente antes de empezar:

* Python 3.x – para ejecutar el script de extracción.
* OpenCV – biblioteca de visión artificial.
* XAMPP – para levantar un servidor local con Apache.

Instala la dependencia de Python con:

```bash
pip install opencv-python
```

# Fase 1: Extracción de Fotogramas (Python)

El script `extraer.py` lee el video y guarda imágenes cada cierto número de fotogramas, listas para ser usadas en software de fotogrametría (Meshroom, RealityCapture, etc.).

## Instrucciones

### 1. Coloca tu video

Copia tu archivo `.mp4` dentro de la carpeta:

```text
VIDEO_PARA_EL_3D/video/
```

### 2. Ejecuta el script

Abre una terminal (CMD, PowerShell o Bash) y navega hasta la carpeta del proyecto:

```bash
cd "ruta\completa\VIDEO_PARA_EL_3D"
python extraer.py
```

### 3. Resultado

Las imágenes se guardarán automáticamente en:

```text
VIDEO_PARA_EL_3D/fotos/
```

con nombres como:

```text
foto_0000.jpg
foto_0001.jpg
foto_0002.jpg
```

# Fase 2: Despliegue en Servidor Local (XAMPP)

Una vez procesadas las imágenes con tu software de fotogrametría y obtenido el modelo 3D (`.obj`, `.gltf`, texturas, etc.), debes montar el visualizador web.

## Pasos

### 1. Copia la carpeta del proyecto

Copia la carpeta `avatar3d` dentro del directorio raíz de XAMPP:

```text
C:\xampp\htdocs\avatar3d\
```

### 2. Enciende Apache

Abre el Panel de Control de XAMPP y haz clic en **Start** junto a **Apache**.

# Fase 3: Visualización en el Navegador

Abre tu navegador favorito (Chrome, Edge o Firefox) y visita:

```text
http://localhost/avatar3d/
```

Si todo está correcto, verás el visualizador interactivo de tu avatar 3D.

## Funcionalidades

* Rotar la cámara con el mouse.
* Hacer zoom con la rueda del ratón.
* Examinar la textura y geometría generadas por fotogrametría.

# Notas Adicionales

* El script `extraer.py` asume que existe un único archivo `.mp4` dentro de `video/`.
* Puedes utilizar cualquier software de fotogrametría. Se recomienda **Meshroom** por ser gratuito y de código abierto.
* Verifica que las rutas de los modelos 3D estén correctamente configuradas en `index.html`.
* Si el visualizador no carga, abre la consola del navegador (`F12`) para revisar posibles errores de rutas.
