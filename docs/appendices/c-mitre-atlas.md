# Appendix C — MITRE ATLAS Mapping Reference

| Attack | MITRE ATLAS Technique |
| --- | --- |
| Prompt Injection | ATLAS T0024 |
| Data Extraction | ATLAS T0015 |
| Training Data Extraction | ATLAS T0002 |
| Model Evasion | ATLAS T0043 |
| Model Poisoning | ATLAS T0031 |
| MCP Tool Poisoning | ATLAS T0024 (Prompt Injection via tool descriptions) + Supply Chain |
| MCP Supply Chain Compromise | ATLAS T0031 (Model Poisoning equivalent) + MITRE ATT&CK T1195 (Supply Chain Compromise) |
| MCP Cross-Server Attack | MITRE ATT&CK T1570 (Lateral Tool Transfer) analog |
| MCP Credential Exposure | MITRE ATT&CK T1552 (Unsecured Credentials) analog |

Security teams should map findings to ATLAS techniques when reporting to ensure compatibility with enterprise threat intelligence programs. MCP-specific attacks may also warrant mapping to traditional MITRE ATT&CK techniques where ATLAS coverage is not yet available.

---
