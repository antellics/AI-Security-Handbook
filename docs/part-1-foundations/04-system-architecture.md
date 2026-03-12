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

---
