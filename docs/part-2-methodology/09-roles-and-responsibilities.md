# 9. Roles and Responsibilities

## 9.1 AppSec / Penetration Testing

AppSec teams focus on **deterministic security validation** of the application integrating the LLM.

Typical responsibilities:

* Prompt injection validation
* Output encoding and sanitization testing
* Authorization boundary validation
* Tenant isolation testing
* RAG retrieval filtering validation
* Tool permission enforcement
* Rate limiting and abuse prevention
* MCP tool description content scanning
* MCP server permission scope validation
* MCP credential exposure assessment
* MCP transport security verification

These tests should be **deterministic and repeatable**, suitable for inclusion in standard penetration testing programs.

## 9.2 Red Team / Adversarial Testing

Red Team exercises focus on **emergent behavior and adversarial manipulation** of AI systems, simulating realistic attacker campaigns.

Typical activities include:

* Advanced jailbreak development
* Multi-turn manipulation attacks
* Long-term prompt poisoning
* AI-driven social engineering
* Tool chaining and lateral movement
* Agent goal hijacking
* Long-con prompt poisoning campaigns
* MCP tool poisoning campaigns
* MCP rug pull and supply chain attacks
* MCP cross-server lateral movement scenarios

These tests simulate **realistic attacker behavior** and may require extended engagement timelines.

---
