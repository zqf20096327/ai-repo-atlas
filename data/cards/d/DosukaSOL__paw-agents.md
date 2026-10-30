# DosukaSOL/paw-agents

⭐ 22 · TypeScript · MIT · 推送 2026-04-22 · [GitHub](https://github.com/DosukaSOL/paw-agents) · 组织维护

**自主 AI agent 框架：把自然语言转为安全可审计的跨渠道行动**

TypeScript 编写的自主 AI agent 运行框架：将自然语言经 INTENT→PLAN→VALIDATE→EXECUTE→VERIFY→LOG 六阶段流水线转化为对 API、浏览器、文件、工作流与外部工具的动作，LLM 仅生成 JSON 计划不直接执行。支持 Telegram/Discord/Slack 等 20+ 渠道、7 家模型供应商（含本地 Ollama）与自动故障切换，三种代理模式（Supervised/Autonomous/Free）配合风险评分、交易模拟与密钥加密。可选集成 Solana 区块链、Purp 智能合约语言与 Jupiter 多 DEX 路由。提供 CLI、Electron 桌面端、移动端、VS Code 与浏览器扩展。自述处于早期 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六阶段执行流水线：LLM 只出计划，系统负责执行与日志
- 20+ 消息渠道与 7 家模型供应商（含免费本地 Ollama）自动故障切换
- 三层代理模式 + 风险评分、交易模拟、AES-256-GCM 密钥加密与 JSONL 审计
- 45+ 内置工具、多 agent 编队、RAG、向量记忆、插件系统与 MCP Server/Client

## 适用场景

- 在 Telegram/Discord 等渠道部署可执行实际操作的 AI agent
- 本地用 Ollama 零 API 费用运行 agent
- 在带交易模拟与确认门控的前提下做 Solana 链上自动化操作

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L36: **PAW Agents** is a production-grade autonomous AI agent framework that converts natural language into safe, valida
> L68: |**Models**|OpenAI, Anthropic, Google AI, Mistral, DeepSeek, Groq, **Ollama (FREE)** — automatic failover|

## 星数曲线

```mermaid
xychart-beta
    title "DosukaSOL/paw-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `25d7552b6d5d` · [字段定义](../../DATASET.md)*
