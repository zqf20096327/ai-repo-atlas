# gbb-acelerators/specky

⭐ 21 · TypeScript · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/gbb-acelerators/specky) · [官网](https://getspecky.ai) · 组织维护

**面向 AI IDE 的规格驱动开发 CLI 工具包：13 agent+58 MCP 工具**

基于 Spec-Kit 方法论的 npm CLI 工具包，将 13 个 agent、22 个 prompt、14 个 skill、16 个 hook 和 58 个 MCP 工具安装到项目中，适配 GitHub Copilot (VS Code)、Claude Code、Cursor 和 OpenCode。通过带签名的阶段图、EARS 六模式需求校验、跨产物对齐检查与前后置 hook，在意图与代码之间执行确定性流水线；支持 GitHub/Azure DevOps/Jira 工作项导出、5 种合规框架证据、Terraform IaC 生成，另有 APM 企业包治理层。需 Node.js 20+，MCP 服务器零外呼、可离线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 agents / 58 MCP tools / 16 hooks 组成的强制流水线
- EARS 六模式需求校验与跨产物（spec→design→task→test）追溯
- Copilot、Claude Code、Cursor、OpenCode 四类 harness 原生适配
- MCP 服务器零外呼，气隙环境可用；MIT 许可

## 适用场景

- 在 AI 编码助手生成代码前先固化需求与验收标准
- 团队按 HIPAA/SOC2/GDPR 等框架留存证据并导出工作项
- 为多 harness 团队统一规格驱动开发流程

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L35: Specky is a **CLI toolkit for Spec-Driven Development** — 13 specialized agents, 58 MCP tools, 22 prompts, 14 skill
> L143: |**MCP**|Model Context Protocol — an open standard that lets AI assistants call external tools|Specky is an MCP se
> L145: |**Agents and Skills**|Specialized AI roles that invoke Specky tools with domain expertise|13 agents + 14 skills o

## 星数曲线

```mermaid
xychart-beta
    title "gbb-acelerators/specky 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `730bab6e073c` · [字段定义](../../DATASET.md)*
