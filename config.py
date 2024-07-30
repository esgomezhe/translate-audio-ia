from dotenv import dotenv_values

# Configuración .env
config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]