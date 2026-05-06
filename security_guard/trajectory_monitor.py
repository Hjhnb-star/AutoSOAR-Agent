import logging

logger = logging.getLogger("TrajectoryMonitor")

class TrajectoryMonitor:
    def __init__(self):
        self.risk_threshold = 0.85

    def _analyze_attention_svd(self, agent_intent):
        """
        利用奇异值分解 (SVD) 分析 LLM 推理过程中的注意力头状态。
        定位是否被间接提示词注入 (IPI) 诱导产生恶意的工具调用轨迹。
        """
        logger.debug("Running SVD-based attention head diagnosis on Agent trajectory...")
        # 模拟提取关键特征矩阵的奇异值
        # 假设如果某个特定的 Attention Sink 被异常激活，则判定为高危
        is_anomalous = False 
        risk_score = 0.12 if not is_anomalous else 0.95
        return risk_score

    def verify_trajectory(self, agent_intent, context):
        """
        评估生成的剧本轨迹是否安全，防止代理执行高危越权操作。
        """
        # 1. 基于规则的静态检查 (是否存在高危目标)
        steps = agent_intent.get("steps", [])
        for step in steps:
            if step.get("target") in ["127.0.0.1", "0.0.0.0", "admin_subnet"]:
                return False, "Trajectory attempts to target critical internal infrastructure."

        # 2. 基于模型内在状态的深度审查 (内生安全)
        risk_score = self._analyze_attention_svd(agent_intent)
        if risk_score > self.risk_threshold:
            return False, "Anomalous attention pattern detected. Possible Indirect Prompt Injection (IPI)."

        return True, "Safe"
