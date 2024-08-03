import os
from uuid import uuid4
import config


def setup_environment(openai_api_key, langchain_api_key):
    unique_id = uuid4().hex[0:8]
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "AI-Assistant"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    # os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    # os.getenv("OPENAI_API_KEY")
    os.environ['OPENAI_API_KEY'] = openai_api_key
