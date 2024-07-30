# Translate IA

Traductor de voz a diferentes idiomas utilizando IA y Gradio para la creación de la UI Web

# Instalación

Para la instalación del entorno virtual y sus respectivos paquetes seguiremos estos comandos:

1. Creación del entorno virtual y su activación:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instalación de los paquetes requeridos:
   ```
   pip install -r requirements.txt
   ```
3. Ejectuar la aplicación (En la carpeta principal):
   ```
   python main.py
   ```
6. Si tienes problemas con fbgemm.dll:
   
   Descarga el siguiente dll: https://www.dllme.com/dll/files/libomp140_x86_64/00637fe34a6043031c9ae4c6cf0a891d/download
   Añade el dll descargado en la carpeta /windows/system32

7. Si tienes problemas con el archivo de audio:

   Descarga ffmpeg: https://ffmpeg.org/download.html#build-windows
   Añadelo al path de windows