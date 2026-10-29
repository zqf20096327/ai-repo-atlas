# adamenrem-jpg/Roblox-Live-Bridge-MCP

⭐ 70 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/adamenrem-jpg/Roblox-Live-Bridge-MCP) · 个人维护

**自托管 MCP 桥接层：让 AI 实时观察并操控 Roblox 等客户端**

NexusForge Client Bridge 是一个自托管的实时中继层，将 AI 推理引擎连接到运行中的应用客户端（首个适配器面向 Roblox）。工作方式为四步循环：适配器推送结构化观察快照，AI 客户端发出高层意图，策略白名单校验并转发意图，全部记录写入 SQLite 账本可回放与比对。面向开发者与研究者，提供 Docker Compose 一键部署、多语言操作台、可插拔 AI 后端（OpenAI 兼容 API、本地 llama.cpp）。架构上中继核、账本写入器、操作台三进程协作，适配器经 WebSocket+JSON 接入。限制：SQLite 单写者模型，高吞吐需规划；安全模型不替代网络层加固。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 观察/意图/授权/回放四原语循环，全部操作入 SQLite 账本
- YAML 声明式意图白名单与按意图限速，支持热重载
- 模块化适配器系统（四个回调接口），任意可讲 WebSocket+JSON 的语言可写
- 本地优先：无外呼遥测，账本单文件可移植，MIT 许可

## 适用场景

- 让本地 AI 在受控白名单内观察并操作 Roblox 客户端会话
- 审计与回放 AI 自动化会话的完整意图与观察记录
- 为新目标运行时编写适配器，扩展 AI 操控范围

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: **A self-hosted, real-time automation bridge that connects AI reasoning engines to live application runtimes — start
> L47: - 🧩 **Pluggable AI Backends** — Supports OpenAI-compatible APIs, local llama.cpp servers, and custom HTTP endpoints
> L58: **1. The Relay Core** — A WebSocket server that speaks a small, versioned protocol. It receives observations from a

## 星数曲线

```mermaid
xychart-beta
    title "adamenrem-jpg/Roblox-Live-Bridge-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-29 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `943ff0385e67` · [字段定义](../../DATASET.md)*
