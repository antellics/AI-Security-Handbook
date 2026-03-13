# 30. Tester Checklists and Quick Reference

## 30.1 AppSec Tester Checklist

- [ ] Prompt injection resistance (direct override, role escalation, priority injection)
- [ ] Output encoding and sanitization
- [ ] RAG access control (document-level permissions)
- [ ] Tool authorization enforcement
- [ ] Context isolation (cross-user, cross-tenant)
- [ ] Session memory isolation
- [ ] Guardrail effectiveness
- [ ] Abuse protections (rate limiting, token caps)
- [ ] Input validation on file uploads and external content
- [ ] MCP tool description scanning for adversarial content
- [ ] MCP tool description change detection (rug pull protection)
- [ ] MCP credential exposure in config files and CLI arguments
- [ ] MCP server permission scoping (least privilege)
- [ ] MCP transport security (authentication, encryption)
- [ ] MCP cross-server invocation policy enforcement
- [ ] MCP tool name uniqueness (shadowing prevention)

## 30.2 Red Team Checklist

- [ ] Advanced jailbreak attempts (roleplay, encoding, multi-step)
- [ ] Multi-turn manipulation and trust building
- [ ] Agent goal hijacking
- [ ] Long-con prompt poisoning
- [ ] Tool chaining attacks
- [ ] RAG poisoning campaigns
- [ ] AI-assisted social engineering
- [ ] Cross-model injection (if multi-model architecture)
- [ ] MCP tool poisoning campaign (malicious server with adversarial tool descriptions)
- [ ] MCP rug pull attack (post-approval tool description modification)
- [ ] MCP tool shadowing (duplicate tool name exploitation)
- [ ] MCP cross-server lateral movement
- [ ] MCP supply chain compromise (malicious third-party server package)
- [ ] MCP credential harvesting via config discovery
- [ ] MCP SSRF through server tool parameters

## 30.3 AI Component Enumeration Checklist

- [ ] Identify all AI-enabled features and interfaces
- [ ] Fingerprint model provider and version
- [ ] Map prompt construction pipeline
- [ ] Enumerate RAG data sources and vector databases
- [ ] Enumerate available tools and their capabilities
- [ ] Identify memory and persistence mechanisms
- [ ] Map trust boundaries between components
- [ ] Document authorization enforcement points
- [ ] Discover MCP configuration files and their contents
- [ ] Enumerate connected MCP servers and their provenance
- [ ] List all MCP tools, resources, and prompt templates
- [ ] Identify MCP transport types (stdio vs. remote HTTP/SSE)
- [ ] Assess MCP server authentication and credential storage
- [ ] Map MCP server permission scopes
- [ ] Check for duplicate tool names across MCP servers
- [ ] Review MCP server package versions and update policies

---
