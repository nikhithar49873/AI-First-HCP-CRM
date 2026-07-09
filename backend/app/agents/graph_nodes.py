from app.ai.groq_client import llm


def choose_tool(state):

    user_input = state["user_input"]

    prompt = f"""
You are an AI CRM assistant.

Choose ONLY ONE tool from this list.

Log Interaction
Edit Interaction
Doctor Lookup
Follow-up Reminder
Meeting Summary

User:

{user_input}

Return ONLY tool name.
"""

    response = llm.invoke(prompt)

    state["selected_tool"] = response.content.strip()

    return state
from app.tools.log_interaction import log_interaction_tool
from app.tools.edit_interaction import edit_interaction_tool
from app.tools.doctor_lookup import doctor_lookup_tool
from app.tools.followup_tool import followup_tool
from app.tools.summary_tool import summary_tool


def execute_tool(state):

    tool = state["selected_tool"]

    text = state["user_input"]

    if "Edit" in tool:

        result = edit_interaction_tool(text)

    elif "Doctor" in tool:

        result = doctor_lookup_tool(text)

    elif "Follow" in tool:

        result = followup_tool(text)

    elif "Summary" in tool:

        result = summary_tool(text)

    else:

        result = log_interaction_tool(text)

    state["result"] = str(result)

    return state