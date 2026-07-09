from app.agents.hcp_agent import run_agent

response = run_agent(
    """
    Met Dr Sharma at Apollo Hospital.

    Specialization Cardiology.

    Discussed Drug A.

    Follow up next Friday.

    Doctor liked the product.
    """
)

print(response)