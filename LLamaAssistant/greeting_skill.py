from skills.basic_skill import BasicSkill
from langchain_core.tools import tool

class GreetingSkill(BasicSkill):
    def __init__(self):
        self.name = "Greeting"
        self.metadata = {
            "name": self.name,
            "description": "Generates a personalized greeting based on the provided name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person to greet."
                    }
                },
                "required": ["name"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    @tool
    def perform(self, name: str) -> str:
        """
        Generate a personalized greeting.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A personalized greeting message.
        """
        return f"Hello, {name}! It's great to meet you. How can I assist you today?"