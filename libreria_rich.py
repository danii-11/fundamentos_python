from rich import print as rprint

nums_tuple = (1,2,3,4)
rprint(nums_tuple)

nums_list = [1,2,3,4]
print(nums_list)

nums_dict = {"nums_list": nums_list, "nums_tuple": nums_tuple}
print(nums_dict)

bool_list = [True, False]
print(bool_list)

# Console -> mas funciones para aplicar estilos al texto
from rich.console import Console
console = Console() # Crear una instancia de Console
console.print("Esto es un texto normal") # Imprimir texto con estilo
console.print("Esto es un texto en negrita", style="bold underline purple") # Imprimir texto en negrita
console.print("Esto es un texto en cursiva", style="italic magenta") # Imprimir texto en cursiva
console.print("Esto es un texto con fondo azul", style="blue on white") # Imprimir texto con fondo azul

# markup -> sistema de marcado [] [/]
console.print("Esto es un texto de [red]ejemplo[/red] para mirar como funciona el sistema de Marcado")

# Texto
from rich.text import Text
texto = Text("Hola, mundo!")
texto.stylize("bold italic underline #00af00", 0, 5) # Aplicar estilo a una parte del texto
console.print(texto)

# Tema 
from rich.theme import Theme
tema_personalizado = Theme({"exito": "bold green", "error": "bold red"})
console = Console(theme=tema_personalizado) # Crear una instancia de Console con el tema personalizado

console.print("¡Operación exitosa!", style="exito") # Imprimir texto con estilo de éxito
console.print("¡Error en la operación!", style="error") # Imprimir texto con estilo de error

# Emojis
console.print("¡Hola! :smile:") # Imprimir texto con emoji
console.print("¡Adiós! :wave:") # Imprimir texto con emoji
console.print("¡Feliz cumpleaños! :birthday:") # Imprimir texto con emoji

# Console.log
import time
from rich.console import Console

console = Console()
for i in range(10):
    console.log(f" Depurando codigo...{i}") # Imprimir mensaje de log
    time.sleep(0.2) 

# Tablas 
from rich.table import Table
tabla = Table(title="LISTA DE TAREAS") # Crear una tabla con un título

# Agregar columnas a la tabla
tabla.add_column("Numero", style="cyan", justify="center") # Agregar una columna a la tabla
tabla.add_column("Tarea", style="magenta", justify="center") 
tabla.add_column("Estado", style="green", justify="center") 

# Agregar filas a la tabla
tabla.add_row("1", "App Consola", "Pendiente")
tabla.add_row("2", "App Web", "En Progreso")
tabla.add_row("3", "App Movil", "Completada")

console.print(tabla) # Imprimir la tabla en la consola

# Barras de progreso
import time
from rich.progress import Progress

with Progress() as progress: # Crear una barra de progreso
    task = progress.add_task("[green]Procesando...", total=100)
    while not progress.finished:
        progress.update(task, advance=0.6)
        time.sleep(0.02)
