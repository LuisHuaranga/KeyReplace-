from pynput import keyboard
import pyperclip  # Librería para manejar el portapapeles

# Diccionario de palabras clave y sus reemplazos
trigger_words = {
    "dp": "a d d.lib.program(CDCB",  #programa
    "ap": "a d a.lib.program(CDCB",
    "ep": "a d e.lib.program(CDCB",
    "dpr": "a d d.lib.proc(CDCP",    #proceso  
    "epr": "a d a.lib.proc(CDCP",
    "epr": "a d e.lib.proc(CDCP",
    "dj": "a d d.lib.job(CDCA",      #job
    "aj": "a d a.lib.job(CDCA",
    "ej": "a d e.lib.job(CDCA",
    "dc": "a d d.lib.copy.cob(",      #copy
    "ac": "a d a.lib.copy.cob(",
    "ec": "a d e.lib.copy.cob(",
    
}
current_text = []
controller = keyboard.Controller()

def on_press(key):
    try:
        if key.char and key.char != '`':
            current_text.append(key.char)
        elif key.char == '`':
            # Unimos el texto actual para compararlo
            current_text_str = ''.join(current_text)
            for trigger_word, replacement_text in trigger_words.items():
                if current_text_str.endswith(trigger_word):
                    # Borrar la palabra clave (simulamos con backspace)
                    for _ in range(len(trigger_word) + 1):
                        controller.press(keyboard.Key.backspace)
                        controller.release(keyboard.Key.backspace)
                    
                    # Copiar el texto de reemplazo al portapapeles
                    pyperclip.copy(replacement_text)
                    
                    # Pegar el texto de reemplazo
                    controller.press(keyboard.Key.ctrl)
                    controller.press('v')
                    controller.release('v')
                    controller.release(keyboard.Key.ctrl)
                    
                    # Limpiar current_text después del reemplazo
                    del current_text[-len(trigger_word):]
                    break  # Salir del bucle si se encuentra una coincidencia
    except AttributeError:
        pass

def on_release(key):
    # Salir del programa si se presiona Esc
    if key == keyboard.Key.esc:
        print("~~~~~~~~~~~~~~~~Fin del programa PIPIPPIPIPI~~~~~~~~~~~~~~~~")
        return False

# Iniciar el listener del teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("-----------------Esperando palabras claves JIJIJIJIJI-----------------")
    listener.join()
