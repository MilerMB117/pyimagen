# Generador de Imágenes a partir de Texto

Esta es una aplicación de Python que utiliza la API de OpenAI para generar imágenes a partir de texto. La interfaz de usuario está construida con Tkinter y las imágenes se manejan con la biblioteca Pillow.

## Requisitos

- Python 3.6 o superior
- Una clave API de OpenAI

## Instalación

1. Clona este repositorio:

    ```bash
    git clone link-repo
    cd pyimagen
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura tu clave API de OpenAI:

    Reemplaza `'TU_CLAVE_API'` en `app.py` con tu clave API de OpenAI.

## Uso

Ejecuta la aplicación:

```bash
python app.py
