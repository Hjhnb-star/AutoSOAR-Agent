import logging
from tools.firewall_api import FirewallAPI
from tools.edr_connector import EDRConnector

logger = logging.getLogger("ExecutionAgent")

class ExecutionAgent:
    def __init__(self):
        self.firewall = FirewallAPI()
        self.edr = EDRConnector()

    def execute(self, playbook):
        results = []
        for step in playbook.get("steps", []):
            action = step.get("action")
            target = step.get("target")
            
            if action == "block_ip":
                res = self.firewall.block_ip(target)
            elif action == "isolate_endpoint":
                res = self.edr.isolate_host(target)
            else:
                res = f"Unknown action: {action}"
                
            logger.info(f"Executed {action} on {target}: {res}")
            results.append({action: res})
        return results
