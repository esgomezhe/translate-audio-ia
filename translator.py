import whisper
from translate import Translator
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
import gradio as gr
from config import ELEVENLABS_API_KEY

def translator(audio_file, selected_language, output_options):

    # 1. Transcribir texto

    # Usamos Whisper: https://github.com/openai/whisper
    # Alternativa API online: https://www.assemblyai.com

    try:
        model = whisper.load_model("small")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error transcribiendo el texto: {str(e)}")

    # 2. Traducir texto

    # Usamos Translate: https://github.com/terryyin/translate-python

    translation = ""
    if selected_language == 'en':
        try:
            translation = Translator(
                from_lang="es", to_lang="en").translate(transcription)
        except Exception as e:
            raise gr.Error(
                f"Se ha producido un error traduciendo el texto a Inglés: {str(e)}")

    elif selected_language == 'it':
        try:
            translation = Translator(
                from_lang="es", to_lang="it").translate(transcription)
        except Exception as e:
            raise gr.Error(
                f"Se ha producido un error traduciendo el texto a Italiano: {str(e)}")

    elif selected_language == 'fr':
        try:
            translation = Translator(
                from_lang="es", to_lang="fr").translate(transcription)
        except Exception as e:
            raise gr.Error(
                f"Se ha producido un error traduciendo el texto a Francés: {str(e)}")

    elif selected_language == 'ja':
        try:
            translation = Translator(
                from_lang="es", to_lang="ja").translate(transcription)
        except Exception as e:
            raise gr.Error(
                f"Se ha producido un error traduciendo el texto a Japonés: {str(e)}")

    outputs = []

    if 'Texto' in output_options:
        outputs.append(translation)
    else:
        outputs.append(None)

    if 'Audio' in output_options:
        # 3. Generar audio traducido

        # Usamos Elevenlabs IO: https://elevenlabs.io/docs/api-reference/getting-started

        save_file_path = text_to_speech(translation, selected_language)
        outputs.append(save_file_path)
    else:
        outputs.append(None)

    return outputs

def text_to_speech(text: str, language: str) -> str:

    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"audio/{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error creando el audio: {str(e)}")

    return save_file_path