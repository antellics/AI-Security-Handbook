# 10. GenAI Security Testing Methodology

The testing methodology consists of four phases executed sequentially.

## Phase 1 — Discovery and Architecture Review

### Step 1 — Identify AI Components

Locate GenAI features within the application:

* Chat assistants and AI copilots
* AI-driven search and document analysis
* Automated summarization and report generation
* AI workflow automation

### Step 2 — Identify Model Architecture

Determine how the model is integrated:

* Direct LLM API usage
* RAG architecture
* Tool-enabled systems
* Agentic frameworks

### Step 3 — Identify Prompt Construction

Analyze how prompts are assembled. Typical structure:

```
System Prompt
Developer Instructions
Retrieved Context
Conversation History
User Input
```

### Step 4 — Map Data Sources

Identify sources used for context retrieval:

* Document repositories
* APIs and databases
* Uploaded files
* Web crawlers

### Step 5 — Enumerate Tools

Determine whether the model can call tools such as:

* Databases and data stores
* Email systems
* Internal APIs
* Cloud resources
* MCP server-provided tools

### Step 5a — Enumerate MCP Servers

If MCP is present, identify:

* Connected MCP servers and their provenance (first-party, third-party, community)
* Tools, resources, and prompt templates exposed by each server
* Transport type for each server (local stdio vs. remote HTTP/SSE)
* Authentication mechanisms and credential storage
* MCP configuration file locations and contents
* Version pinning and update policies for MCP server packages

## Phase 2 — Trust Boundary Analysis

### Step 6 — Identify Trust Boundaries

Locate entry points where untrusted input enters the system:

* Chat input fields
* File uploads
* External content sources
* API endpoints
* Third-party integrations
* MCP server connections (each server is a trust boundary)
* MCP tool descriptions injected into prompt context
* MCP resources providing external data to the model

### Step 7 — Evaluate Authorization Controls

Verify enforcement of:

* User isolation
* Tenant isolation
* Document permissions
* Tool authorization
* Session boundaries
* MCP server permission scoping
* MCP tool invocation authorization per user role
* MCP credential isolation between servers

### Step 8 — Evaluate Prompt Security

Review defenses such as:

* Prompt templates and instruction isolation
* Guardrail policies
* Structured prompts
* Input sanitization

## Phase 3 — Exploitation Testing

### Step 9 — Prompt Injection

Attempt to override system instructions through direct and indirect injection.

### Step 10 — Data Exfiltration

Attempt extraction of system prompts, secrets, internal documents, and other user data.

### Step 11 — Tool Abuse

Manipulate model tool calls to perform unauthorized actions. For MCP-enabled systems, test tool poisoning, rug pulls, shadowing, cross-server influence, and credential exposure.

### Step 12 — Output Injection

Test whether generated output can exploit downstream systems through HTML, markdown, or script injection.

## Phase 4 — Advanced Adversarial Testing

### Step 13 — Jailbreak Testing

Attempt bypassing guardrails through roleplay, encoding, multi-step manipulation, and persona switching.

### Step 14 — Multi-Turn Manipulation

Test gradual trust building and progressive prompt conditioning across conversation turns.

### Step 15 — Abuse Testing

Evaluate operational abuse including token exhaustion, cost amplification, and tool flooding.

---
