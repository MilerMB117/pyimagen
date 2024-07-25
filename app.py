import openai
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import io

# Configura tu clave API de OpenAI
openai.api_key = 'CLAVE_API'

def generar_imagen(texto):
    try:
        # Usar DALL-E para generar la imagen
        response = openai.Image.create(
            prompt=texto,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        image_response = requests.get(image_url)
        img = Image.open(io.BytesIO(image_response.content))
        return img
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def mostrar_imagen():
    texto = entry.get()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un texto.")
        return

    img = generar_imagen(texto)
    if img:
        img.thumbnail((256, 256))
        img_tk = ImageTk.PhotoImage(img)
        label_img.config(image=img_tk)
        label_img.image = img_tk

        # Guardar imagen
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img.save(file_path, "PNG")
            messagebox.showinfo("Guardado", f"Imagen guardada en {file_path}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Imágenes a partir de Texto")

# Crear y colocar widgets
label = tk.Label(ventana, text="Ingresa el texto:")
label.pack(pady=5)

entry = tk.Entry(ventana, width=50)
entry.pack(pady=5)

boton = tk.Button(ventana, text="Generar Imagen", command=mostrar_imagen)
boton.pack(pady=10)

label_img = tk.Label(ventana)
label_img.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
