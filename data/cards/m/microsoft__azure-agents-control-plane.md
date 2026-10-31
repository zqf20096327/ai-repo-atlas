# microsoft/azure-agents-control-plane

⭐ 24 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/microsoft/azure-agents-control-plane) · 组织维护

**微软的 AI agent 全生命周期企业治理控制平面参考实现**

面向企业 AI agent 开发的治理方案仓库：以 Azure API Management 作为共享治理边界，集中管理身份认证、鉴权、限流与请求遥测；通过用户分配托管身份、Entra Agent ID 与 Agents 365 注册中心实现 agent 注册、所有权核验和禁用开关。包含 AKS 托管的 MCP agent 参考后端，用 azd up 一键部署 AKS、APIM 与 MCP 服务，支持 Python/TypeScript 两种运行时，并遵循 SpecKit 规范驱动开发方法。Fabric 专家组件默认禁用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- APIM 作为跨平台（含 Copilot Studio/Power Platform）agent 访问的统一治理边界
- Agents 365 注册中心提供 agent 身份清单与 Disable 治理开关
- 托管身份 + Entra Agent ID 联邦的身份优先安全模型，无需存储客户端密钥
- azd up 一键部署 AKS/APIM/MCP 服务，Python 与 TypeScript 双运行时

## 适用场景

- 企业统一治理分散在 Copilot Studio、Power Platform 等平台的 AI agent 访问
- 为 agent 建立注册、所有权核验与集中禁用的治理流程
- 部署 AKS 托管的 MCP agent 参考后端并接入 Azure AI 服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: The Azure Agents Control Plane governs the complete lifecycle of enterprise AI agents: analysis, design, development
> L13: - **API-First Agent Architecture** - All agent operations flow through Azure API Management with Model Context Prot
> L19: Keep agents where they are built and hosted; use APIM as the shared governance

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/azure-agents-control-plane 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `79fed89bab26` · [字段定义](../../DATASET.md)*
