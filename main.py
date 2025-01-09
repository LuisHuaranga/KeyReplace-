from pynput import keyboard
import pyperclip  # Librería para manejar el portapapeles

programa = "CDCB102"

# Diccionario de palabras clave y sus reemplazos
trigger_words = {
    "pr": programa,
    "srt": "411997",                        #numero SRT
    "luis": "S38457.LUIS.SRT11997",         #bibliotecaPersonal
    "aco": f"C:\\Users\\HP\\Desktop\\Decomiso\\Grupo-4\\compilaciones\\{programa}.txt",
    "luisp": f"S38457.LUIS.SRT11997({programa})",         #bibliotecaPersonal
    "rexp": f"EXP DSN=S38457.LIB.PROGRAM({programa})",         #bibliotecaPersonal
    "comp": f"SPRCC1.ISSYS.COMP.D.TIP012.{programa}.COBOL63",
    "dp": "a d d.lib.program(",             #programa
    "ap": "a d a.lib.program(",
    "ep": "a d e.lib.program(",
    "dpr": "a d d.lib.proc(",               #proceso   
    "epr": "a d a.lib.proc(",
    "epr": "a d e.lib.proc(",
    "dj": "a d d.lib.job(A",                #job
    "aj": "a d a.lib.job(",
    "ej": "a d e.lib.job(",
    "dc": "a d d.lib.copy.cob(",            #copy
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
    if key == keyboard.Key.pause:
        print(f"~~~~~~~~~~~~~~~~Fin del programa PROGRAMA ACTUAL: {programa}~~~~~~~~~~~~~~~~")
        return False

# Iniciar el listener del teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("~~~~~~~~~~~~~~~~Esperando palabras PROGRAMA ACTUAL: {programa} claves JIJIJIJIJI~~~~~~~~~~~~~~~~")    
    listener.join()


