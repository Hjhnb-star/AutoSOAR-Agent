from core.llm_engine import LLMEngine
from core.prompt_templates import TRIAGE_PROMPT
import json

class TriageAgent:
    def __init__(self):
        self.llm = LLMEngine()

    def analyze(self, raw_alert):
        prompt = TRIAGE_PROMPT.format(raw_data=json.dumps(raw_alert))
        response = self.llm.generate(prompt=prompt, system_prompt="Triage")
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"threat_type": "Unknown", "severity": "Low"}
