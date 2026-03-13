# 2. Scope and Objectives

## 2.1 In Scope

This standard applies to any application integrating AI models within its architecture, including:

* LLM-based chat interfaces and customer support chatbots
* AI copilots embedded in software products
* AI-powered enterprise search systems
* RAG-based knowledge assistants
* LLM-powered automation and workflow orchestration systems
* AI agents capable of executing tools or APIs
* AI-driven document analysis and report generation systems
* Automated summarization features
* MCP-enabled AI applications connecting to external tools and data sources via the Model Context Protocol
* MCP servers exposing tools, resources, or prompts to AI clients

## 2.2 Out of Scope

The following areas are excluded unless explicitly included in the engagement scope:

* Base model training security and infrastructure
* Model weight extraction attacks against providers
* GPU infrastructure hardening
* AI model alignment research
* Model supply chain validation

## 2.3 Objectives

Security testing should aim to identify:

* Prompt injection vulnerabilities (direct and indirect)
* Data leakage and exfiltration risks
* Authorization boundary failures
* Tool misuse or abuse
* Rendering and output vulnerabilities
* Knowledge base poisoning risks
* Business logic manipulation through AI systems
* Behavioral manipulation and guardrail bypass
* Resource abuse and cost amplification vectors
* MCP server trust boundary violations and tool poisoning
* MCP cross-server attack propagation
* MCP credential and transport security weaknesses

---
