from app.ai.groq_client import llm

response = llm.invoke(
    "Say hello in one sentence."
)

print(response.content)

