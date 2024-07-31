import streamlit as st
from langchain_app.environment import setup_environment
from langchain_app.agent import setup_agent, invoke_agent


def main():
    st.title("LangChain Assistant")

    # API Key inputs
    openai_api_key = st.text_input(
        "Enter your OpenAI API Key:", type="password")
    langchain_api_key = st.text_input(
        "Enter your LangChain API Key:", type="password")

    if st.button("Set API Keys"):
        st.session_state["OPENAI_API_KEY"] = openai_api_key
        st.session_state["LANGCHAIN_API_KEY"] = langchain_api_key
        st.success("API Keys set successfully!")
        setup_environment(
            st.session_state["OPENAI_API_KEY"], st.session_state["LANGCHAIN_API_KEY"])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    query = st.text_input("Enter your query:")

    if st.button("Submit"):
        if "OPENAI_API_KEY" not in st.session_state or "LANGCHAIN_API_KEY" not in st.session_state:
            st.error("Please set both OpenAI and LangChain API keys.")
        else:
            agent = setup_agent()
            response = invoke_agent(agent, query)
            st.session_state.messages.append(
                {"query": query, "response": response})

    if st.session_state.messages:
        for message in st.session_state.messages:
            st.write(f"**You:** {message['query']}")
            st.write(f"**Assistant:** {message['response']}")


if __name__ == "__main__":
    main()
