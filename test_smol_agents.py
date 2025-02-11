from smolagents import TransformersModel, CodeAgent, DuckDuckGoSearchTool

model = TransformersModel(
    model_id="Qwen/Qwen2-0.5B-Instruct",
    max_new_tokens=4096,
    device_map="auto"
)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How long in seconds would it take for a leopard at full speed to run through Pont Des Arts?")