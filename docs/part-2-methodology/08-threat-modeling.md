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
| MCP Tool Poisoning | Hidden instructions in tool descriptions |
| MCP Rug Pull | Server changes tool behavior after approval |
| MCP Tool Shadowing | Malicious server overrides legitimate tools |
| MCP Supply Chain | Compromised third-party MCP server |
| MCP Credential Exposure | API keys in MCP configs or transport |
| MCP Cross-Server Attack | One server influences calls to another |

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

### MCP Security

* What MCP servers are connected? Are any third-party or community-maintained?
* Are MCP tool descriptions reviewed before injection into the prompt context?
* Can MCP servers change tool descriptions or behavior after initial approval (rug pull)?
* Are MCP server connections authenticated and encrypted?
* Are credentials (API keys, tokens, connection strings) exposed in MCP configuration files?
* Can a malicious MCP server register tools that shadow legitimate tools from other servers?
* Is the permission scope of each MCP server minimally scoped?
* Are MCP tool invocations logged with server identity and full parameters?
* Can MCP resources deliver adversarial content into the prompt context?
* Is there a review/approval process for adding new MCP servers?
* Are MCP server packages pinned to specific versions or pulled from unverified sources?
* Can one MCP server's tool influence the invocation of another server's tool?

## 8.4 Threat Modeling Template

| Component | Risk | Attack Example |
| --- | --- | --- |
| Prompt Builder | Prompt injection | Instruction override |
| Vector Store | Knowledge poisoning | Malicious document |
| LLM | Guardrail bypass | Jailbreak |
| Tool Layer | Privilege escalation | Forced tool use |
| Output Renderer | XSS | HTML injection |
| MCP Server | Tool poisoning | Hidden instructions in tool descriptions |
| MCP Server | Rug pull | Post-approval behavior change |
| MCP Server | Tool shadowing | Name collision with legitimate tools |
| MCP Transport | Credential exposure | API keys in config or CLI args |
| MCP Supply Chain | Server compromise | Malicious third-party package |

---
