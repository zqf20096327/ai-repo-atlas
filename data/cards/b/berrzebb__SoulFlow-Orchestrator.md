# berrzebb/SoulFlow-Orchestrator

⭐ 22 · TypeScript · NOASSERTION · 推送 2026-03-24 · [GitHub](https://github.com/berrzebb/SoulFlow-Orchestrator) · 个人维护

**自托管多云 AI agent 运行时：多渠道消息+工作流编排**

TypeScript 实现的自托管 AI agent 编排运行时，接收 Slack/Telegram/Discord/网页聊天消息，由 8 个角色 agent 团队处理，支持自然语言生成 DAG 工作流（141 种节点、HITL 审批门）。提供 9 种可切换的 agent 后端（Claude/Codex/Gemini/OpenAI 兼容/OpenRouter/Ollama 等），CircuitBreaker 自动故障切换，支持纯本地 Ollama 运行。敏感信息经 AES-256-GCM Vault 加密，数据存储在本地 SQLite。另可作为 MCP 服务器桥接 Claude Code/Cursor。需 Docker/Podman 运行，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种 provider 中立 agent 后端，CircuitBreaker 自动切换
- 141 节点工作流引擎 + 188 个确定性工具，HITL 审批门
- AES-256-GCM Vault 敏感信息加密，数据仅存本地 SQLite
- MCP 桥接模式向 Claude Code/Cursor 暴露 56 个项目管理工具

## 适用场景

- 在自有服务器上搭建连接 Slack/Telegram/Discord 的多 agent 团队
- 用自然语言生成多阶段工作流并经人工审批后执行
- 在 IDE 中通过 MCP 调用项目管理（看板/工作流/记忆）工具

## 场景标签

`多智能体` `工作流自动化` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L29: 9개 에이전트 백엔드는 CircuitBreaker가 자동 관리합니다 — 코드 수정 없이 프로바이더 교체, 완전 로컬(Ollama only) 운영 모두 가능합니다.
> L80: |**MCP 서버 브리지**|Claude Code · Cursor 등 AI 개발 도구 연동|56개 프로젝트 관리 도구 MCP 노출|
> L91: `claude_sdk` · `claude_cli` · `codex_appserver` · `codex_cli` · `gemini_cli` · `openai_compatible` · `openrouter` ·

## 星数曲线

```mermaid
xychart-beta
    title "berrzebb/SoulFlow-Orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `498688d0d2e3` · [字段定义](../../DATASET.md)*
