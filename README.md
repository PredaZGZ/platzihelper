# Platzi Helper
Este código permite recopilar y consultar información sobre preguntas y respuestas. Al ejecutar el código, se le preguntará al usuario si desea recopilar o consultar información.

## Modo de recopilación
Para recopilar información, se le pedirá al usuario que elija entre copiar el html desde el portapapeles o desde un archivo.

Una vez seleccionado el modo de recopilación, se procesará el html y se extraerán las preguntas y respuestas correctas e incorrectas. Esta información se guardará en un archivo llamado "ans.pkl" utilizando la librería "pickle".

## Modo de consulta
Para consultar información, se le pedirá al usuario que ingrese una pregunta. El código buscará en el archivo "ans.pkl" una pregunta similar a la ingresada y mostrará la respuesta correcta y las respuestas incorrectas asociadas a esa pregunta.

El código utiliza la librería "difflib" para comparar la similitud entre las preguntas y determinar si se trata de la misma pregunta o no. Si se encuentra una pregunta similar con una similitud mayor al 90%, se considera que se trata de la misma pregunta y se muestra la información asociada.

Si no se encuentra una pregunta similar en el archivo "ans.pkl", se informará al usuario que no se ha encontrado ninguna coincidencia.

## Librerías utilizadas
- jaraco.clipboard: permite copiar el html desde el portapapeles
- bs4: permite procesar el html y extraer información
- tkinter.filedialog: permite seleccionar un archivo
- pickle: permite guardar y cargar información en un archivo
- difflib: permite comparar la similitud entre cadenas de texto
