# omega-memory/omega-memory

⭐ 224 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/omega-memory/omega-memory) · [官网](https://omegamax.co) · 组织维护

**本地优先的 AI 编程代理跨模型持久记忆 MCP 服务器**

以 MCP 服务器形式为 AI 编程代理提供跨会话持久记忆：存储决策、教训、偏好等记忆条目，用本地 ONNX 嵌入模型（bge-small-en-v1.5）做语义检索，SQLite 存储于 ~/.omega，配合 Claude Code hooks 实现自动捕获与浮现，也支持 Cursor、Windsurf、Cline 等 MCP 客户端，另可作 Python 库使用。完全本地运行，无需云服务或 API key。核心开源（Apache 2.0），免费版在 2,000 条记忆后降级为文本匹配、5,000 条停止存储，多代理协调、LLM 路由、知识库等模块属 OMEGA Pro 付费功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 ONNX 嵌入模型实现语义搜索，数据存于本机 SQLite
- 通过 Claude Code hooks 自动捕获会话决策并浮现相关记忆
- 提供约 15 个 MCP 工具（存储/检索/时间线/检查点/矛盾检测等）与完整 CLI
- 可作为 Python 库用于脚本与 CI/CD

## 适用场景

- 让 Claude Code、Cursor 等编程代理跨会话记住决策与偏好
- 多代理协作时通过 Pro 模块做文件锁与任务队列
- 作为 Python 库在自动化脚本中存取记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Cross-model memory for AI agents. Local-first. Works with Claude, GPT, Gemini, Cursor, Claw Code, and any MCP clie
> L160: ## MCP Tools Reference

## 星数曲线

```mermaid
xychart-beta
    title "omega-memory/omega-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 223 --> 226
    line [225, 224]
```

2026-10-18 225 → 2026-10-24 224（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9090fa059fff` · [字段定义](../../DATASET.md)*
