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

## A.4 MCP Exploitation Attack Tree

```
MCP Server Connection
      │
      ├── Tool Poisoning
      │       │
      │       ├── Hidden Instructions in Tool Descriptions
      │       │       │
      │       │       ├── Data Exfiltration via Other Servers
      │       │       ├── Credential Harvesting (SSH keys, env vars)
      │       │       └── System Prompt Override
      │       │
      │       └── Adversarial Metadata in Tool Schema
      │
      ├── Rug Pull
      │       │
      │       ├── Post-Approval Description Modification
      │       └── Server-Side Execution Logic Change
      │
      ├── Tool Shadowing
      │       │
      │       ├── Duplicate Tool Name Registration
      │       └── Invocation Hijacking
      │
      ├── Cross-Server Attacks
      │       │
      │       ├── Lateral Tool Invocation
      │       │       │
      │       │       ├── Filesystem Access via Legitimate Server
      │       │       ├── Database Query via Legitimate Server
      │       │       └── Network Access via Legitimate Server
      │       │
      │       └── Cross-Server Data Exfiltration
      │               │
      │               ├── Aggregate Data from Multiple Servers
      │               └── Route Data Through Server with External Access
      │
      ├── Supply Chain
      │       │
      │       ├── Typosquatting Server Packages
      │       ├── Compromised Maintainer Account
      │       └── Malicious Package Update
      │
      ├── Credential Exposure
      │       │
      │       ├── Config File Discovery
      │       ├── CLI Argument Extraction
      │       └── Transport Token Interception
      │
      ├── Resource Poisoning
      │       │
      │       ├── Adversarial Content in MCP Resources
      │       └── Prompt Template Manipulation
      │
      └── Server-Side Request Forgery
              │
              ├── Internal Network Scanning
              ├── Cloud Metadata Access
              └── Local File Read
```

---
