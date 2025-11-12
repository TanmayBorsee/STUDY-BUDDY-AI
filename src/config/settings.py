import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = "llama-3.1-8b-instant"
    
    TEMPERATURE = 0.9 # to be more creative in responses

    MAX_RETRIES = 3 # number of retries for API calls so that transient errors can be handled


settings = Settings()  