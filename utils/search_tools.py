from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


def get_search_tool():
    return DuckDuckGoSearchAPIWrapper()
