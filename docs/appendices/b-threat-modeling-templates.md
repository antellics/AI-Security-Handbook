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

## B.2 Data Flow Threat Template

For each data flow in the AI system, document:

1. **Source:** Where does the data originate?
2. **Trust Level:** Is the source trusted, semi-trusted, or untrusted?
3. **Processing:** How is the data transformed or used?
4. **Destination:** Where does the data go?
5. **Controls:** What validation, filtering, or authorization exists?
6. **Threats:** What attacks are possible at this point?

---
