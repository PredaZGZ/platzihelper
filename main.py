from jaraco import clipboard

cb = clipboard.paste_html()


# Print the clipboard contents
print(cb)

with open("mi_archivo.txt", "w") as f:
    # Escribe el contenido de la variable en el archivo
    f.write(cb)