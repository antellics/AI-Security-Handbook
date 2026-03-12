# 8. Threat Modeling AI Systems

Security teams should threat-model AI systems using structured analysis that accounts for the unique properties of probabilistic, prompt-driven systems.

## 8.1 AI Trust Boundary Model

```
User Input
    ↓
Application Layer
    ↓
Prompt Construction
    ↓
RAG Retrieval
    ↓
LLM
    ↓
Tool Invocation
    ↓
External Systems
```

Each transition between layers represents a trust boundary. Vulnerabilities most commonly occur at these boundaries.

## 8.2 Primary Threat Categories

| Category | Example |
| --- | --- |
| Prompt Injection | Instruction override |
| Context Leakage | Cross-user data exposure |
| Tool Abuse | Unauthorized database queries |
| Output Injection | Script injection in responses |
| Resource Abuse | Token exhaustion |
| Knowledge Poisoning | Malicious document injection |

## 8.3 Threat Modeling Questions

### Prompt Security

* Can user input override system instructions?
* Are prompts isolated by role (system vs. user)?
* Are prompt templates used consistently?

### RAG Security

* Can malicious documents be uploaded?
* Are retrieved documents filtered by user permissions?
* Is document provenance tracked?

### Tool Security

* Are tool permissions enforced per user role?
* Are tool parameters validated against allowlists?
* Are tool invocations logged and auditable?

### Context Security

* Can the model access other users' data?
* Is session isolation enforced?
* Does conversation memory leak across sessions?

## 8.4 Threat Modeling Template

| Component | Risk | Attack Example |
| --- | --- | --- |
| Prompt Builder | Prompt injection | Instruction override |
| Vector Store | Knowledge poisoning | Malicious document |
| LLM | Guardrail bypass | Jailbreak |
| Tool Layer | Privilege escalation | Forced tool use |
| Output Renderer | XSS | HTML injection |

---
