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

## 28.6 Context and Memory Isolation

* Enforce strict session isolation between users
* Implement tenant-level data separation
* Scope conversation memory to the current session by default
* Review memory persistence mechanisms for cross-session leakage
* Validate memory contents before injection into prompts

---
