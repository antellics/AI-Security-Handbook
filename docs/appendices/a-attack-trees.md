# Appendix A — Attack Trees

## A.1 Prompt Injection Attack Tree

```
User Input
   │
   ├── Direct Prompt Injection
   │       │
   │       ├── System Prompt Disclosure
   │       ├── Guardrail Bypass
   │       ├── Tool Invocation
   │       └── Behavioral Manipulation
   │
   └── Indirect Prompt Injection
           │
           ├── Malicious Document
           ├── Poisoned Web Content
           ├── Knowledge Base Poisoning
           └── Hidden Text in Uploaded Files
```

## A.2 RAG Exploitation Attack Tree

```
Knowledge Base
    │
    ├── Malicious Document Injection
    │
    ├── Embedding Poisoning
    │
    ├── Retrieval Ranking Manipulation
    │
    ├── Persistent Knowledge Poisoning
    │
    └── Prompt Execution via Retrieved Context
```

## A.3 Agent Exploitation Attack Tree

```
Prompt Injection
      │
      ├── Goal Hijacking
      │
      ├── Tool Invocation
      │       │
      │       ├── Database Access
      │       ├── API Calls
      │       └── File Operations
      │
      ├── Tool Chaining
      │       │
      │       ├── Data Retrieval
      │       ├── Data Transformation
      │       └── External Exfiltration
      │
      └── Persistence
              │
              ├── Memory Planting
              └── Knowledge Poisoning
```

---
