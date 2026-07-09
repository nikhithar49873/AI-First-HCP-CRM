from app.tools.log_interaction import log_interaction_tool
from app.tools.edit_interaction import edit_interaction_tool
from app.tools.doctor_lookup import doctor_lookup_tool
from app.tools.followup_tool import followup_tool
from app.tools.summary_tool import summary_tool


def run_agent(user_input):

    message = user_input.lower()

    if "edit" in message:

        return edit_interaction_tool(user_input)

    elif "summary" in message:

        return summary_tool(user_input)

    elif "follow" in message:

        return followup_tool(user_input)

    elif "doctor" in message:

        return doctor_lookup_tool(user_input)

    else:

        return log_interaction_tool(user_input)