# 29. Risk Rating and Reporting

## 29.1 Risk Severity Classification

| Severity | Description | Example |
| --- | --- | --- |
| Critical | Unauthorized system actions or sensitive data exposure at scale | Tool abuse enabling cross-tenant data exfiltration |
| High | Guardrail bypass enabling harmful actions or significant data exposure | System prompt exposure revealing secrets, persistent RAG poisoning |
| Medium | Partial information leakage or moderate guardrail bypass | Guardrail bypass without direct impact, markdown injection |
| Low | Behavior manipulation without direct business impact | Minor jailbreak with no data exposure, cosmetic output manipulation |

## 29.2 Reporting Template

Each finding should include:

**Title:** Clear description of the vulnerability

**Description:** Technical explanation of the issue

**Attack Vector:** How the vulnerability is exploited

**Proof-of-Concept Prompt:** The exact prompt or sequence used

**Reproduction Steps:** Step-by-step instructions to reproduce

**Affected Components:** Which layers or components are vulnerable

**Business Impact:** Real-world consequences of exploitation

**Exploitability:** Required access level and attacker skill

**Reproducibility:** Whether the issue reproduces consistently (important for non-deterministic AI systems)

**Recommended Mitigation:** Specific remediation guidance

AI vulnerabilities often require contextual explanation due to non-deterministic behavior. Document the success rate across multiple attempts when findings are probabilistic.

---
