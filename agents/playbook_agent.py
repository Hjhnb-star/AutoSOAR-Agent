from core.llm_engine import LLMEngine
from core.prompt_templates import PLAYBOOK_GEN_PROMPT
import json

class PlaybookAgent:
    def __init__(self):
        self.llm = LLMEngine()

    def generate_playbook(self, context):
        prompt = PLAYBOOK_GEN_PROMPT.format(context=json.dumps(context))
        response = self.llm.generate(prompt=prompt, system_prompt="Playbook")
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"id": "error", "steps": []}
