# 26. Red Team Campaign Playbooks

Red teams should simulate **realistic attacker campaigns** that combine multiple techniques across the kill chain. These playbooks demonstrate end-to-end attack scenarios.

## 26.1 Data Exfiltration Campaign

**Objective:** Extract sensitive internal data through the AI system.

**Steps:**

1. **Reconnaissance:** Probe the system to identify available tools, data sources, and boundaries
2. **Prompt Injection:** Override system instructions to establish attacker influence
3. **Tool Invocation:** Trigger internal database queries or API calls
4. **Data Retrieval:** Extract internal data through tool responses
5. **Encoding:** Encode retrieved data if output filtering is present
6. **Exfiltration:** Extract data through model responses or tool-assisted external channels

## 26.2 RAG Poisoning Campaign

**Objective:** Establish persistent influence over model behavior through knowledge base manipulation.

**Steps:**

1. **Document Preparation:** Create a malicious document containing embedded instructions
2. **Upload:** Submit the document through available ingestion channels
3. **Indexing Wait:** Allow time for the document to be indexed in the vector store
4. **Trigger Retrieval:** Craft queries that cause the malicious document to be retrieved
5. **Execution:** Embedded prompt injection executes via the retrieved context
6. **Persistence Verification:** Confirm the attack persists across sessions and users

## 26.3 Agent Compromise Campaign

**Objective:** Hijack an AI agent to perform unauthorized actions.

**Steps:**

1. **Prompt Injection:** Inject instructions to override the agent's current objective
2. **Goal Hijacking:** Redirect the agent's planning toward attacker-defined goals
3. **Tool Invocation:** Agent executes unauthorized tool calls under attacker influence
4. **Data Exfiltration:** Agent retrieves and returns sensitive data
5. **Persistence:** Attempt to plant instructions in agent memory for future sessions

---
