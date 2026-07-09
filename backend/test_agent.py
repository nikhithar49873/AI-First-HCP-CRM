from app.agents.hcp_agent import run_agent

response = run_agent(
    "Met Dr Sharma today and discussed Drug B."
)

print(response)