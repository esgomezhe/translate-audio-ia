import gradio as gr
from translator import translator

web = gr.Interface(
    fn=translator,
    inputs=[
        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Español"
        ),
        gr.Radio(
            choices=["en", "it", "fr", "ja"],
            label="Selecciona el idioma para traducir",
            value="en"  # Por defecto, selecciona inglés
        ),
        gr.CheckboxGroup(
            choices=["Texto", "Audio"],
            label="Selecciona el tipo de salida",
            value=["Texto"]  # Por defecto, selecciona texto
        )
    ],
    outputs=[
        gr.Textbox(label="Texto traducido"),
        gr.Audio(label="Traducción de audio")
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()