from langgraph.graph import StateGraph, END

from app.agents.graph_state import AgentState
from app.agents.graph_nodes import (
    choose_tool,
    execute_tool
)

workflow = StateGraph(AgentState)

workflow.add_node(
    "choose_tool",
    choose_tool
)

workflow.add_node(
    "execute_tool",
    execute_tool
)

workflow.set_entry_point(
    "choose_tool"
)

workflow.add_edge(
    "choose_tool",
    "execute_tool"
)

workflow.add_edge(
    "execute_tool",
    END
)

graph = workflow.compile()


def run_agent(user_input):

    state = {

        "user_input": user_input,

        "selected_tool": "",

        "result": ""

    }

    return graph.invoke(state)