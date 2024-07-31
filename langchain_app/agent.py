from langchain.chains import LLMMathChain
from langchain_core.tools import Tool
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain_openai import ChatOpenAI, OpenAI

from utils.search_tools import get_search_tool
from utils.math_tools import get_math_tool


def setup_agent():
    search = get_search_tool()
    llm_math_chain = get_math_tool()

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
    ]

    model = ChatOpenAI(model_name='gpt-4o-mini', temperature=0)
    planner = load_chat_planner(model)
    executor = load_agent_executor(model, tools, verbose=True)
    agent = PlanAndExecute(planner=planner, executor=executor)

    return agent


def invoke_agent(agent, query):
    return agent.invoke(query)
