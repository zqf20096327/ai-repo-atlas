# greeves89/AI-Employee

⭐ 18 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/greeves89/AI-Employee) · [官网](https://github.com/greeves89/AI-Employee) · 个人维护

**面向团队的自托管多 Agent 平台：每 Agent 独立容器+治理审计**

自托管多 Agent 平台，每个 Agent 运行在独立 Docker 容器中，拥有自己的工作区、记忆与规则；支持 Claude Code、OpenAI Codex CLI 及自带 harness 三种运行时，可接入 Azure、Bedrock、Vertex、Ollama、LM Studio 等模型。提供自主权限矩阵（Allow/Ask/Deny）、审批、审计日志、DLP 出站过滤与预算控制；语义记忆用本地 bge-m3 嵌入。面向 DACH 地区中小企业与受监管组织，DSGVO 导向；私有免费，商用按许可收费（Starter 149€/月起）。安装需 git clone 加 setup.sh 与 Docker Compose。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 Agent 独立 Docker 容器与资源限制
- 三种运行时（Claude Code / Codex CLI / 通用 harness）统一工具与审批
- Allow/Ask/Deny 自主权限矩阵与人审审批
- 本地 bge-m3 语义记忆，不外发嵌入 API

## 适用场景

- 团队在自有服务器上运行多个专职 AI Agent 并保留数据
- 为受监管组织提供带审计日志与 DSGVO 特性的 Agent 运行环境
- 通过 Telegram/Teams/Slack 等渠道与 Agent 协作并走审批流程

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **The self-hosted multi-agent AI platform for teams that need governance, traceability and data they keep.**
> L32: **AI-Employee gives every agent its own isolated Docker container, memory, knowledge and rules, on a server you con
> L101: - **Three runtimes, one feature set** — Claude Code, OpenAI Codex CLI, and a built-in harness for any other model 

## 星数曲线

```mermaid
xychart-beta
    title "greeves89/AI-Employee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `55631d20f184` · [字段定义](../../DATASET.md)*
