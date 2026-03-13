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

## 26.4 MCP Tool Poisoning Campaign

**Objective:** Compromise an MCP-enabled application through a malicious MCP server to exfiltrate sensitive data.

**Steps:**

1. **Reconnaissance:** Identify target application's MCP integration (IDE, chat client, agent platform)
2. **Server Preparation:** Create a malicious MCP server package with benign-appearing tools whose descriptions contain hidden adversarial instructions
3. **Distribution:** Publish the MCP server to a package registry (npm, PyPI) with a plausible name and description, or distribute via social engineering (blog post, tutorial, forum recommendation)
4. **Installation:** Target user installs and connects the MCP server, approving its listed tools
5. **Tool Poisoning Activation:** Hidden instructions in tool descriptions manipulate the LLM to exfiltrate data through other connected MCP servers or include sensitive context in tool call parameters
6. **Cross-Server Pivot:** Leverage tool descriptions that instruct the model to invoke filesystem, database, or network tools from other connected servers
7. **Data Exfiltration:** Sensitive data (SSH keys, environment variables, source code, credentials) is transmitted through the malicious server's tool invocation parameters or a controlled external endpoint
8. **Persistence:** Optionally, poison MCP resources or prompt templates that persist beyond the current session

## 26.5 MCP Rug Pull Campaign

**Objective:** Establish trust with a legitimate-appearing MCP server, then modify behavior to compromise the application.

**Steps:**

1. **Trust Building:** Publish a genuinely useful MCP server with clean tool descriptions and build user adoption
2. **Reputation Establishment:** Accumulate downloads, positive reviews, and integrations
3. **Rug Pull:** Push an update that modifies tool descriptions to include adversarial instructions, or change server-side execution logic to exfiltrate tool parameters
4. **Exploitation:** Users who auto-update or reinstall receive the compromised version
5. **Lateral Impact:** Compromised tool descriptions influence model behavior across all users of the server

## 26.6 MCP Cross-Server Lateral Movement Campaign

**Objective:** Use a low-privilege MCP server to escalate access through other connected servers.

**Steps:**

1. **Initial Access:** Gain control of a single MCP server connection (via tool poisoning or supply chain)
2. **Server Enumeration:** Use tool description directives to instruct the model to list all connected MCP servers and their tools
3. **Capability Mapping:** Identify high-value tools on other servers (filesystem access, database queries, email sending, cloud APIs)
4. **Cross-Server Exploitation:** Craft tool description directives that instruct the model to invoke high-value tools on other servers with attacker-controlled parameters
5. **Data Collection:** Aggregate sensitive data retrieved from multiple servers
6. **Exfiltration:** Route collected data through a server with external network access

---
