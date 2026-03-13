# 3. Terminology and Definitions

### System Prompt

Hidden instructions defining the behavior and constraints of the model. These are set by the application and are not intended to be visible to end users.

### Developer Prompt

Instructions embedded by application developers within the prompt chain to guide model responses toward specific behaviors or formats.

### User Prompt

Input submitted directly by the end user through the application interface.

### Retrieved Context

External content injected into the prompt during RAG workflows, typically drawn from document repositories, knowledge bases, or vector databases.

### Memory

Conversation or session history used to influence model responses across turns. May persist within a session or across sessions depending on implementation.

### Guardrails

Safety mechanisms, policies, or filtering systems designed to prevent restricted, unsafe, or off-topic outputs from the model.

### Agent

An LLM system capable of autonomously planning tasks, reasoning about objectives, and executing actions through tool invocations.

### Tool Invocation

When an LLM triggers external APIs, functions, databases, or automation systems to perform actions or retrieve information.

### Orchestration Layer

Application logic responsible for building prompts, coordinating model interactions, managing conversation flow, and routing tool calls.

### Vector Store

A database used to store embeddings (dense numerical representations) for semantic similarity retrieval in RAG systems.

### Output Rendering Layer

User interfaces and downstream systems that display, store, or process model responses.

### Prompt Construction Layer

The application layer responsible for assembling the final prompt from system instructions, developer instructions, retrieved context, and user input.

### Model Context Protocol (MCP)

An open protocol that standardizes how AI applications connect to external tools, data sources, and services. MCP defines a client-server architecture where AI hosts connect to MCP servers that expose capabilities through a uniform interface.

### MCP Host

An AI-enabled application (IDE, chat client, AI agent platform) that initiates connections to MCP servers. The host runs one or more MCP clients and controls which servers are connected and what permissions are granted.

### MCP Client

A protocol client within the host application that maintains a stateful session with a single MCP server. The client negotiates capabilities, routes tool calls, and manages the lifecycle of the connection.

### MCP Server

A lightweight program or service that exposes tools, resources, and prompt templates to MCP clients via the standardized protocol. Servers can run locally (over stdio) or remotely (over HTTP with Server-Sent Events). Servers may be first-party, third-party, or community-maintained.

### MCP Tool

A function exposed by an MCP server that the LLM can invoke. Tools have names, descriptions, and JSON Schema parameter definitions. Tool descriptions are visible to the model and influence its behavior.

### MCP Resource

A data source exposed by an MCP server that provides context to the model. Resources are identified by URIs and can represent files, database records, API responses, or other structured data.

### Tool Poisoning

An attack where a malicious MCP server embeds hidden adversarial instructions within tool descriptions or metadata that manipulate model behavior when the tool listing is injected into the prompt context.

### Rug Pull

An attack where an MCP server changes the behavior or description of its tools after the user has approved the initial connection, exploiting the gap between what was reviewed and what is executed.

### Tool Shadowing

An attack where a malicious MCP server registers tools with names identical or similar to those exposed by legitimate servers, intercepting or overriding intended tool invocations.

---
