import streamlit as st
from langchain_app.environment import setup_environment
from langchain_app.agent import setup_agent, invoke_agent


def main():
    st.set_page_config(page_title="LangChain Assistant",
                       page_icon=":robot_face:")

    # Sidebar layout
    st.sidebar.title("LangChain Assistant")
    st.sidebar.write("Please enter your API keys:")

    openai_api_key = st.sidebar.text_input("OpenAI API Key:", type="password")
    langchain_api_key = st.sidebar.text_input(
        "LangChain API Key:", type="password")

    if st.sidebar.button("Set API Keys"):
        if not openai_api_key or not langchain_api_key:
            st.sidebar.error(
                "Both OpenAI and LangChain API keys must be provided.")
        else:
            try:
                st.session_state["OPENAI_API_KEY"] = openai_api_key
                st.session_state["LANGCHAIN_API_KEY"] = langchain_api_key
                setup_environment(
                    st.session_state["OPENAI_API_KEY"], st.session_state["LANGCHAIN_API_KEY"])
                st.sidebar.success("API Keys set successfully!")
            except Exception as e:
                st.sidebar.error(f"Error setting API keys: {e}")

    st.title("Chat with LangChain Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    query = st.text_input("Enter your query:")

    if st.button("Submit"):
        if not query:
            st.error("Query must not be empty.")
        elif "OPENAI_API_KEY" not in st.session_state or "LANGCHAIN_API_KEY" not in st.session_state:
            st.error(
                "Please set both OpenAI and LangChain API keys in the sidebar.")
        else:
            try:
                agent = setup_agent()
                response = invoke_agent(agent, query)
                st.session_state.messages.append(
                    {"query": query, "response": response})
            except Exception as e:
                st.error(f"Error invoking the agent: {e}")

    if st.session_state.messages:
        for message in st.session_state.messages:
            st.write(f"**You:** {message['query']}")
            st.write(f"**Assistant:** {message['response']}")


if __name__ == "__main__":
    main()
