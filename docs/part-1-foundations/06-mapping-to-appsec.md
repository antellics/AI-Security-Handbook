# 6. Mapping GenAI Vulnerabilities to Traditional AppSec

GenAI vulnerabilities largely correspond to traditional web application security weaknesses, expressed through new interaction patterns.

| Traditional Vulnerability | GenAI Equivalent | Description |
| --- | --- | --- |
| Injection (SQLi, Command) | Prompt Injection | User instructions override system instructions |
| Cross-Site Scripting (XSS) | Output Injection | Malicious model output executed in UI or downstream systems |
| Access Control Failures | Context Leakage | Model exposes unauthorized data across users or tenants |
| Sensitive Data Exposure | Model Data Leakage | Secrets, system prompts, or internal data exposed through prompts |
| SSRF / API Abuse | Tool Invocation Abuse | LLM triggers unauthorized internal APIs or system actions |
| Input Validation Failures | RAG Poisoning | Malicious content injected into knowledge bases |
| Business Logic Abuse | Jailbreak / Model Manipulation | Model behavior manipulated to bypass intended workflows |

This mapping allows security teams to leverage existing AppSec expertise when testing AI-enabled applications.

---
