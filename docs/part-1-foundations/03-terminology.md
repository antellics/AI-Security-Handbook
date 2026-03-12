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

---
