import os, sys

#para guardar imagens no .exe. Fonte: https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)