class IPIDefender:
    @staticmethod
    def sanitize_input(raw_text):
        # 清洗可能包含恶意指令的外部输入
        forbidden_tokens = ["Ignore previous instructions", "System override"]
        for token in forbidden_tokens:
            raw_text = raw_text.replace(token, "[REDACTED]")
        return raw_text
