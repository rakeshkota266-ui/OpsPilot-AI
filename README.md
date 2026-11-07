# OpsPilot AI 🚀

### Multi-Agent AI-Powered IT Incident Response Platform

OpsPilot AI is a collaborative multi-agent incident response workflow built using **Switch AI** and **Mattermost**. Four specialized AI agents work together to triage incidents, investigate possible root causes, recommend remediation, and verify recovery.

## 🎯 Problem Statement

IT teams often spend valuable time coordinating incident response across different teams and tools. OpsPilot AI demonstrates how specialized AI agents can collaborate in a shared workspace to organize incident response and support faster, evidence-based decisions.

## 🤖 Multi-Agent Architecture

| Agent | Responsibility |
|---|---|
| Triage Agent | Classifies incident severity and business impact |
| Investigation Agent | Identifies root-cause hypotheses and required evidence |
| Resolution Agent | Recommends remediation and rollback plans |
| Verification Agent | Defines independent recovery checks and success criteria |

## 🔄 Workflow

1. Incident is reported.
2. Triage Agent assesses severity.
3. Investigation Agent identifies possible root causes.
4. Resolution Agent prepares conditional remediation options.
5. Verification Agent reviews recovery criteria.
6. Agents share findings and produce a consolidated incident report.
7. Human approval is required before risky production actions.

## 🛠️ Technology Stack

- Switch AI — Multi-agent coordination
- Mattermost — Shared incident response workspace
- OpenCode — Agent execution provider
- Docker Desktop — Local container environment
- YAML — Reusable room configuration

## 🔐 Safety and Human Approval

- No unauthorized production changes.
- Verified facts are separated from assumptions.
- No invented telemetry or test results.
- Human approval required before risky actions.
- Incidents remain open until independent verification.

## 🧪 Demonstration

The team tested the workflow using a simulated incident:

**INC-001: Company website unavailable and customers unable to log in.**

All four agents produced findings and collaborated on a remediation and verification plan.

The incident remained OPEN because no real infrastructure telemetry or recovery evidence was available. This was a simulated demonstration, not a real production incident.

## 📌 Current Project Status

- [x] Four specialized agents created.
- [x] Agents added to a shared Mattermost room.
- [x] Individual agent responses tested.
- [x] Resolution plan reviewed by Verification Agent.
- [x] Consolidated incident report generated.
- [x] Room configuration captured as a reusable template.
- [ ] Automated incident intake and structured handoffs.
- [ ] Integration with real monitoring and infrastructure tools.
- [ ] End-to-end automated verification.

## 👥 Team

**Team Technova**

Built for the Flip the Switch Hackathon.

## 📄 License

To be determined.
## 🎬 Project Demo

Watch the OpsPilot AI demonstration video:

[OpsPilot AI – Hackathon Demo](./OpsPilot_AI_Demo.mp4)

The demonstration covers the Flask incident dashboard, the four specialized AI agents, their individual responses in Mattermost, and the evidence-based verification process.

**Demo outcome:** 0 passed, 0 failed, 5 untested. The simulated incident remains OPEN. No production changes were executed.

**Current limitation:** The Flask dashboard is not directly integrated with Switch AI. The agents were demonstrated individually through the shared Mattermost channel.
