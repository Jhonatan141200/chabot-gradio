import gradio as gr
from gradio_client import Client
from custom_greetings import listDespedidas, listSaludos

#Golpeamos la web Api
def chatbot(input_text, history):
    client = Client("http://localhost:8008/")
    result = client.predict(
                    input_text,	
                    api_name="/qa"
    )
    for texto1 in listSaludos:
          if texto1.upper() == input_text.upper():
              return "Hola, ¡ Soy Bible Bot ! ¿En que te ayudo?"
    for texto2 in listDespedidas:
          if texto2.upper()  == input_text.upper() :
              return "Nos vemos Pronto, no olvides que si quiere saprender más, te esperamos en Jr Independencia 875"
    return result


#Creamos una interface de Gradio de tipo ChatBot (Gradio ya tiene plantillas realizadas)
iface = gr.ChatInterface(chatbot,
                        title="Bible Bot  IASD Trujillo",
                        theme='soft',
                        examples=["¿Cúal es el verdadero día de reposo? ¿Por que?",
                                  "¿Qué es la Fe?", 
                                  "¿Qué es la oración?", 
                                  "¿Cómo nos comunicamos con Dios?", 
                                  "¿Dios escucha las oraciones?", 
                                  "¿Qué es la Iglesia Adventista?",
                                  "¿Qué es la biblia?",
                                  "¿Caules son los Diez Mandamientos?", 
                                   "¿Que pasa cuando una persona muere? ¿A donde va?",
                                  "¿Podemos comunicarnos con los muertos?",
                                  "¿Cúal es el carácter de Dios?", 
                                  "¿Existe el Purgatorio?", 
                                  "¿Cuál es el sello de Dios?", 
                                  "¿Cómo debemos bautizarnos?", 
                                  "¿A qué se compara la biblia?"],
                        cache_examples=False,
                        retry_btn=None,
                        undo_btn=None,
                        clear_btn=None,
                        submit_btn="Preguntar")


#Corremos Gradio con una Login por defecto
iface.launch(share=True, 
             auth=("admin", "admin"), 
             auth_message="BIENVENIDO A BIBLE CHATBOT", 
             show_error="Credencailes incorrectas")