from translate import Translator

def translate_spanish_to_english(text):
    translator = Translator(to_lang="en", from_lang="es")
    translation = translator.translate(text)
    return translation

# Ejemplo de uso
spanish_text = "Hola, ¿cómo estás?"
translated_text = translate_spanish_to_english(spanish_text)
print(translated_text)