# 28. Defensive Architecture Review

Security teams reviewing AI-enabled applications should evaluate the following defensive controls:

## 28.1 Secure Prompt Construction

* Use structured prompt templates that separate system, developer, and user segments
* Implement instruction isolation to prevent user input from being interpreted as system instructions
* Avoid embedding secrets, credentials, or sensitive configuration in prompts
* Use parameterized prompt construction rather than string concatenation

## 28.2 RAG Security Controls

* Implement access control on document retrieval — enforce user permissions at query time
* Scan documents at ingestion for adversarial content, hidden text, and imperative instructions
* Track document provenance and maintain approval workflows for knowledge base updates
* Classify documents by sensitivity and filter retrieval based on classification
* Monitor for retrieval behavior drift after ingestion events

## 28.3 Tool Authorization Controls

* Enforce per-user and per-role tool authorization policies
* Validate tool parameters against allowlists
* Implement approval gates for high-impact actions
* Log all tool invocations with full context (caller, parameters, result)
* Implement per-session tool usage quotas

## 28.4 Output Rendering Security

* Sanitize all model output before rendering in UI
* Use safe markdown renderers that strip unsafe schemes (javascript:, data:)
* Implement Content Security Policy (CSP) headers
* Scan stored model output for persistent injection risks
* Validate links and citations in model responses

## 28.5 Abuse and Resource Controls

* Set maximum output token limits per request
* Implement per-session and per-user cost quotas
* Add rate limiting on model invocations
* Monitor token usage for anomalies
* Implement adaptive throttling for abusive patterns

## 28.6 MCP Security Controls

### MCP Server Trust Management

* Maintain an allowlist of approved MCP servers with verified provenance
* Require security review before connecting new MCP servers, especially third-party or community-maintained servers
* Pin MCP server packages to specific versions — do not auto-update without review
* Verify package integrity using checksums or provenance attestation
* Implement an organizational approval workflow for MCP server additions

### MCP Tool Description Security

* Scan tool descriptions for adversarial content, imperative instructions, hidden directives, and prompt injection patterns before injecting them into the prompt context
* Hash tool descriptions at approval time and detect changes on subsequent connections (rug pull detection)
* Reject or flag tool descriptions containing suspicious patterns (e.g., instructions targeting other tools, encoded content, references to sensitive files)
* Display full tool descriptions to users during approval, not just tool names

### MCP Transport Security

* Use authenticated and encrypted transports for remote MCP servers (HTTPS with TLS)
* Validate server identity for remote connections
* Prefer local (stdio) transport for sensitive operations where possible
* Never expose MCP server endpoints to untrusted networks without authentication

### MCP Credential Protection

* Never pass credentials (API keys, tokens, connection strings) as command-line arguments to MCP servers — use environment variables or secure credential stores
* Scan MCP configuration files for exposed secrets
* Rotate credentials used by MCP servers on a regular schedule
* Isolate credentials between MCP servers — each server should use dedicated credentials scoped to its function

### MCP Permission Scoping

* Apply the principle of least privilege to each MCP server — scope access to the minimum required resources
* For filesystem MCP servers, restrict access to specific directories rather than granting broad filesystem access
* For database MCP servers, use read-only credentials unless write access is explicitly required
* Implement per-user permission mapping for MCP tool invocations

### MCP Cross-Server Isolation

* Implement policies that prevent one MCP server's tool descriptions from influencing invocations to other servers
* Monitor and alert on cross-server tool invocation chains
* Consider server-level sandboxing to prevent lateral movement
* Implement approval gates for tool chains that span multiple MCP servers

### MCP Monitoring and Logging

* Log all MCP tool invocations with server identity, tool name, parameters, and caller context
* Monitor for tool description changes across sessions
* Alert on new MCP server connections, especially from unrecognized sources
* Track cross-server invocation patterns for anomaly detection
* Monitor MCP server network egress for unexpected outbound connections

## 28.7 Context and Memory Isolation

* Enforce strict session isolation between users
* Implement tenant-level data separation
* Scope conversation memory to the current session by default
* Review memory persistence mechanisms for cross-session leakage
* Validate memory contents before injection into prompts

---
