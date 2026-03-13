# 4. GenAI System Architecture

Most GenAI-enabled applications follow a layered architecture. Understanding this architecture is essential for identifying attack surfaces.

### Typical Architecture

```
User Input
    ↓
Web Application / API
    ↓
Prompt Construction Layer
    ↓
Retrieved Context (RAG)
    ↓
LLM Provider
    ↓
Tool Invocation Layer
    ↓
Application Logic
    ↓
Output Rendering
```

### MCP-Enabled Architecture

Systems using the Model Context Protocol add a standardized integration layer between the LLM and external capabilities:

```
User Input
    ↓
AI Host Application (IDE / Chat Client / Agent Platform)
    ↓
MCP Client(s)
    ↓                          ↓                        ↓
MCP Server A              MCP Server B             MCP Server C
(Local filesystem)        (Database connector)     (Third-party SaaS)
    ↓                          ↓                        ↓
Local Files               Database                 External API
```

In MCP architectures, the host application discovers available tools and resources from connected MCP servers and injects their descriptions into the LLM's prompt context. The LLM then decides which tools to invoke, and the host routes the invocation to the appropriate MCP server. This creates trust boundaries at each MCP server connection, at the tool description injection point, and at the tool execution boundary.

### Prompt Structure

Prompts are typically assembled from multiple components in a defined order:

```
System Prompt
Developer Instructions
Retrieved Context (RAG)
Conversation History (Memory)
User Input
```

The relative positioning and isolation of these components directly affects the system's vulnerability to injection attacks.

### Common Integration Patterns

| Pattern | Description | Key Risk |
| --- | --- | --- |
| Direct LLM API | Application sends prompts directly to an LLM API | Prompt injection |
| RAG Pipeline | Documents retrieved and injected into prompt context | Indirect injection, knowledge poisoning |
| Tool-Enabled | LLM can call external tools, APIs, or databases | Unauthorized actions |
| Agentic Framework | LLM plans and executes multi-step tasks autonomously | Goal hijacking, attack chains |
| Multi-Model | Multiple models chained together for different tasks | Cross-model injection |
| MCP-Integrated | LLM connects to external tools and data via MCP servers | Tool poisoning, rug pulls, cross-server attacks, supply chain compromise |

---
