import sys
import os
from tkinter import Tk

# Agregar el directorio raíz del proyecto al sys.path para asegurar que los módulos se importen correctamente
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), "..."))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)

from gui.login import abrir_ventana_login
from gui.principal import abrir_ventana_principal

def main():
    """Función principal que maneja el ciclo de vida de la aplicación."""
    root = Tk()
    root.withdraw()  # Ocultar la ventana raíz de Tkinter

    # Función para abrir la ventana principal
    def abrir_principal(usuario_id):
        abrir_ventana_principal(usuario_id, reiniciar_aplicacion)

    # Función para reiniciar la aplicación (volver al login)
    def reiniciar_aplicacion():
        root.destroy()  # Cierra la ventana actual
        main()  # Reinicia la aplicación

    # Abrir la ventana de login y pasar la función de retorno
    abrir_ventana_login(abrir_principal)

    root.mainloop()

if __name__ == "__main__":
    main()