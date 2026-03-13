# 5. AI Attack Surface Model

Each layer of a GenAI system introduces a distinct attack surface.

```
User Input
  ↓
Prompt Builder         → Prompt injection, instruction override
  ↓
RAG Retrieval          → Knowledge poisoning, retrieval manipulation
  ↓
MCP Server Layer       → Tool poisoning, rug pulls, shadowing, supply chain
  ↓
LLM Model              → Guardrail bypass, jailbreak
  ↓
Tool Invocation        → Unauthorized execution, parameter manipulation
  ↓
Application Logic      → Business logic abuse, workflow manipulation
  ↓
Output Rendering       → XSS, markdown injection, phishing
```

### AI Threat Model Summary

| Layer | Risk |
| --- | --- |
| User Input | Prompt injection |
| Prompt Builder | Instruction override |
| RAG Retrieval | Knowledge poisoning |
| MCP Servers | Tool poisoning, rug pulls, cross-server attacks |
| MCP Transport | Credential interception, unauthorized server access |
| LLM | Guardrail bypass |
| Tools | Unauthorized execution |
| Rendering | Output injection |

Security testing should evaluate **each layer independently** and also assess how layers interact to enable multi-stage attacks.

---
