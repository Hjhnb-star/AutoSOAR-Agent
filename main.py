import json
import logging
from agents.triage_agent import TriageAgent
from agents.playbook_agent import PlaybookAgent
from agents.execution_agent import ExecutionAgent
from security_guard.trajectory_monitor import TrajectoryMonitor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AutoSOAR-Orchestrator")

class SOAROrchestrator:
    def __init__(self):
        self.triage_agent = TriageAgent()
        self.playbook_agent = PlaybookAgent()
        self.execution_agent = ExecutionAgent()
        self.security_guard = TrajectoryMonitor()

    def process_security_alert(self, raw_alert_data):
        logger.info("🟢 Initiating Multi-Agent SOAR Workflow...")

        context = self.triage_agent.analyze(raw_alert_data)
        logger.info(f"🔍 Triage Complete. Threat: {context.get('threat_type')}")

        playbook = self.playbook_agent.generate_playbook(context)
        logger.info("📝 Dynamic Playbook Generated.")

        is_safe, risk_reason = self.security_guard.verify_trajectory(playbook, context)

        if not is_safe:
            logger.error(f"🚨 Endogenous Security Block: {risk_reason}")
            return {"status": "blocked", "reason": risk_reason}

        logger.info("🛡️ Trajectory Safe. Executing automated response...")
        execution_results = self.execution_agent.execute(playbook)
        
        return {
            "status": "success",
            "playbook_id": playbook.get("id"),
            "results": execution_results
        }

if __name__ == "__main__":
    mock_alert = {
        "source_ip": "192.168.1.105",
        "event_type": "Suspicious_Process_Creation",
        "raw_log": "powershell.exe -w hidden -enc JABzAD0..."
    }
    
    orchestrator = SOAROrchestrator()
    report = orchestrator.process_security_alert(mock_alert)
    print("\n--- Final Report ---")
    print(json.dumps(report, indent=2, ensure_ascii=False))
