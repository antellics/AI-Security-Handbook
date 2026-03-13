# Appendix E — Future AI Attack Classes

Emerging attack classes that security teams should monitor:

* **Autonomous malware agents** — AI systems programmed to autonomously discover and exploit vulnerabilities
* **AI decision manipulation** — Subtle influence on AI-driven business decisions without triggering safety filters
* **Model backdoors** — Hidden behaviors embedded during fine-tuning that activate under specific conditions
* **Supply chain poisoning** — Compromise of model weights, training data, or fine-tuning datasets before deployment
* **Cross-model injection** — Attacks that propagate through multi-model architectures where one model's output feeds another
* **Federated learning attacks** — Poisoning distributed training processes
* **MCP ecosystem attacks** — As MCP adoption grows, large-scale attacks targeting popular MCP server packages to compromise thousands of installations simultaneously, analogous to npm/PyPI supply chain attacks
* **MCP server worms** — Malicious MCP servers that use cross-server influence to propagate adversarial instructions to other connected servers, creating self-spreading compromises across MCP-enabled environments
* **MCP marketplace poisoning** — Attacks targeting MCP server registries and marketplaces where servers are discovered and installed, compromising the discovery and distribution infrastructure
* **Adversarial MCP protocol extensions** — Exploiting future MCP protocol features (sampling, multi-turn server interactions) to establish covert channels or persistent influence over model behavior
* **MCP credential relay attacks** — Chaining compromised MCP servers to relay stolen credentials across organizational boundaries, using one organization's MCP infrastructure to pivot into another's
* **MCP-enabled AI agent botnets** — Coordinated compromise of AI agents through MCP tool poisoning to create networks of compromised agents that can be directed to perform distributed attacks

These categories represent the next frontier of AI security and should be factored into long-term security strategy.

---

*End of Handbook*
