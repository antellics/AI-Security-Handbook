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

## 30.2 Red Team Checklist

- [ ] Advanced jailbreak attempts (roleplay, encoding, multi-step)
- [ ] Multi-turn manipulation and trust building
- [ ] Agent goal hijacking
- [ ] Long-con prompt poisoning
- [ ] Tool chaining attacks
- [ ] RAG poisoning campaigns
- [ ] AI-assisted social engineering
- [ ] Cross-model injection (if multi-model architecture)

## 30.3 AI Component Enumeration Checklist

- [ ] Identify all AI-enabled features and interfaces
- [ ] Fingerprint model provider and version
- [ ] Map prompt construction pipeline
- [ ] Enumerate RAG data sources and vector databases
- [ ] Enumerate available tools and their capabilities
- [ ] Identify memory and persistence mechanisms
- [ ] Map trust boundaries between components
- [ ] Document authorization enforcement points

---
