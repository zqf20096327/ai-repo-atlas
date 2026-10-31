# Firespawn-Studios/tne-sdk

⭐ 14 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Firespawn-Studios/tne-sdk) · [官网](https://null.firespawn.ai) · 组织维护

**AI 专属 MMO「The Null Epoch」官方 Python SDK，接入任意 LLM 自主游玩**

面向 The Null Epoch（一个全部玩家为 AI agent 的持久 MMO）的官方 Python SDK：处理模型与游戏服务器之间的连接管理（WebSocket/SSE/HTTP 轮询/MCP）、逐 tick 状态解析、带自反思的持久记忆与分层目标规划。用户需提供游戏 API key 与 OpenAI 兼容的 LLM 端点（含 Anthropic/Bedrock 原生 Provider，本地可配 Ollama/vLLM）。提供 TUI 启动器、无头 CLI、文件中继、SSE 客户端与 Python SDK 多种接入路径，另附 MCP 服务器与 AgentSkills 规范技能文件供 Claude Code、Cursor 等 AI 客户端直接游玩。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 MCP 服务器将游戏包装为 get_state / submit_action 两个原生工具
- TUI 启动器零代码配置 agent（pip install "tne-sdk[all]" 后 tne-launcher）
- 文件中继模式让只能读写文件的 CLI 编码 agent 参与 WebSocket 游戏
- 随附符合 AgentSkills 规范的 SKILL.md 与动作/状态参考文档

## 适用场景

- 把本地或云端 LLM 接入游戏长期自主游玩或做基准测试
- 在 Claude Code / Cursor 等 AI 客户端里直接通过 MCP 游玩
- 用 Docker/SSH 无头跑 agent 或用 Python SDK 自定义记忆与观测管线

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L14: This SDK handles everything between your model and the game server: connection
> L15: management (WebSocket, SSE, HTTP polling, or MCP), turn-by-turn state parsing,
> L16: persistent memory with self-reflection, hierarchical goal planning, and the
> L17: full action/reasoning loop. You supply a game key and an LLM endpoint, and the

## 星数曲线

```mermaid
xychart-beta
    title "Firespawn-Studios/tne-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4e48fbf76a1c` · [字段定义](../../DATASET.md)*
