from pynput import keyboard

# Diccionario de palabras clave y sus reemplazos
trigger_words = {
    "addlpd": "a d d.lib.program(",
    "ab": "replacement1",
    "a1": "replacement2"
}
current_text = []

def on_press(key):
    try:
        # Solo agregamos letras, números y espacios
        if key.char:
            current_text.append(key.char)
    except AttributeError:
        # Si se presiona Tab, verifica si alguna palabra clave está presente
        if key == keyboard.Key.tab:
            # Unimos el texto actual para compararlo
            current_text_str = ''.join(current_text)
            for trigger_word, replacement_text in trigger_words.items():
                if current_text_str.endswith(trigger_word):
                    # Borrar la palabra clave
                    for _ in range(len(trigger_word)+1):
                        keyboard.Controller().press(keyboard.Key.backspace)
                        keyboard.Controller().release(keyboard.Key.backspace)
                    
                    # Escribir el texto de reemplazo
                    for char in replacement_text:
                        keyboard.Controller().press(char)
                        keyboard.Controller().release(char)
                    
                    # Limpiar current_text después del reemplazo
                    del current_text[-len(trigger_word):]
                    break  # Salir del bucle si se encuentra una coincidencia

def on_release(key):
    # Salir del programa si se presiona Esc
    if key == keyboard.Key.esc:
        return False

# Iniciar el listener del teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
