# Appendix B — Threat Modeling Templates

## B.1 AI System Threat Assessment Template

| Component | Risk Level | Attack Vector | Potential Impact | Current Controls | Gap |
| --- | --- | --- | --- | --- | --- |
| Prompt Builder | | | | | |
| RAG Pipeline | | | | | |
| Vector Store | | | | | |
| LLM Provider | | | | | |
| Tool Layer | | | | | |
| Agent Planner | | | | | |
| Output Renderer | | | | | |
| Memory System | | | | | |
| MCP Server (per server) | | | | | |
| MCP Transport | | | | | |
| MCP Supply Chain | | | | | |

## B.2 Data Flow Threat Template

For each data flow in the AI system, document:

1. **Source:** Where does the data originate?
2. **Trust Level:** Is the source trusted, semi-trusted, or untrusted?
3. **Processing:** How is the data transformed or used?
4. **Destination:** Where does the data go?
5. **Controls:** What validation, filtering, or authorization exists?
6. **Threats:** What attacks are possible at this point?

## B.3 MCP Server Threat Assessment Template

For each connected MCP server, document:

| Field | Value |
| --- | --- |
| Server Name | |
| Server Package / Source | |
| Package Version | |
| Provenance | First-party / Third-party / Community |
| Transport Type | stdio / HTTP+SSE |
| Authentication Method | |
| Credential Storage | |
| Tools Exposed | |
| Resources Exposed | |
| Prompt Templates Exposed | |
| Permission Scope | |
| Network Access | Local only / Internet access |
| Tool Description Reviewed | Yes / No |
| Tool Description Hash | |
| Last Review Date | |
| Cross-Server Dependencies | |
| Risk Level | |
| Known Threats | Tool poisoning, rug pull, shadowing, SSRF, supply chain |
| Current Controls | |
| Gaps | |

---
