from langchain.chains import LLMMathChain
from langchain_openai import OpenAI


def get_math_tool():
    llm = OpenAI(temperature=0)
    return LLMMathChain.from_llm(llm=llm, verbose=True)
