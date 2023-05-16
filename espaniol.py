# from translate import Translator

# def translate_english_to_spanish(text):
#     translator = Translator(to_lang="es")
#     translation = translator.translate(text)
#     return translation

# # Ejemplo de uso
# english_text = "Hello, how are you?"
# translated_text = translate_english_to_spanish(english_text)
# print(translated_text)
import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration
from translate import Translator

@st.cache_resource
def get_models():
    # it may be necessary for other frameworks to cache the model
    # seems pytorch keeps an internal state of the conversation
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


if "history" not in st.session_state:
    st.session_state.history = []

st.title("Hola Chatbot")

# Función para traducir el texto de español a inglés
def translate_to_english(text):
    translator = Translator(to_lang="en", from_lang="es")
    translation = translator.translate(text)
    return translation

# Función para traducir el resultado de la conversación del modelo de inglés a español
def translate_to_spanish(text):
    translator = Translator(to_lang="es")
    translation = translator.translate(text)
    return translation

def generate_answer():
    tokenizer, model = get_models()
    user_message = st.session_state.input_text
    
    
    inputs = tokenizer(translate_to_english(st.session_state.input_text), return_tensors="pt")

    result = model.generate(**inputs)

    message_bot = tokenizer.decode(
        result[0], skip_special_tokens=True
    )  # .replace("<s>", "").replace("</s>", "")
    message_bot = translate_to_spanish(message_bot)

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})


st.text_input("Pone tu mensaje", key="input_text", on_change=generate_answer)
# titulo = translate_to_english("como estas")
# ingles = translate_to_spanish("how are you?")
# st.write(titulo)
# st.write(ingles)
for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i)) #unpacking
