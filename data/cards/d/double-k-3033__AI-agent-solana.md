# double-k-3033/AI-agent-solana

⭐ 18 · Python · MIT · 推送 2025-11-24 · [GitHub](https://github.com/double-k-3033/AI-agent-solana) · [官网](https://solana-agent.com) · 个人维护

**面向 Solana 区块链的 Python AI Agent 框架**

用 Python 构建 AI agent 的框架：以 JSON 定义单 agent 或多 agent swarm，支持按领域专长智能路由、多模态流式输出（文本/音频/图像，含实时双模态）、工具调用与 MCP（一等支持 Zapier）、Solana 区块链工具、知识库（Pinecone，PDF 分块）、输入输出 Guardrails、对话记忆（MongoDB/Zep 可选）与 agentic forms。模型提供方为 OpenAI（gpt-4.1、embedding、realtime、TTS、STT）。实时模式仅支持单 agent；压缩音频输入需 ffmpeg。pip 安装，附 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三行代码启动，JSON 定义 agent，支持多 agent swarm 与智能路由
- 多模态流式：文本/音频/图像，实时双模态（音频+文本同时输出）
- MCP 工具支持（一等支持 Zapier）与 Solana 区块链工具集
- 内置 PII scrubber 的输入输出 Guardrails 与知识库（PDF 分块+语义检索）

## 适用场景

- 我想构建能查询 Solana 钱包余额并执行链上操作的 AI agent
- 我想做多 agent 客服/问答系统并按领域自动路由
- 我想给 agent 接入 MCP 工具（如 Zapier 发邮件）组成自动化工作流

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: ## AI Agents for Solana
> L15: Build your AI agents in three lines of code!
> L75: * Powerful tool integration using standard Python packages and/or inline tools

## 星数曲线

```mermaid
xychart-beta
    title "double-k-3033/AI-agent-solana 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `724bf5bccf9b` · [字段定义](../../DATASET.md)*
