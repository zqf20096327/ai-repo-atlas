# HaseebKhalid1507/SynapsCLI

⭐ 52 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/HaseebKhalid1507/SynapsCLI) · 个人维护

**Rust 编写的终端原生 AI agent 运行时，多 agent 并行与守护进程**

用 Rust 编写的终端 agent 运行时，以单个 25MB 二进制运行：后台 daemon 持有引擎与会话，终端 UI 是薄客户端，多个终端可共享同一实时会话，会话可跨窗口存活。支持并行多 agent 编排、/auto 自主驱动、synaps watcher 舰队监督（心跳/崩溃恢复/成本上限），可接 Claude、ChatGPT、Azure/Bedrock/Vertex、任意 OpenAI 兼容端点及本地 Ollama。凭据经类型化 broker 保管，agent 只获得短时效 token。扩展为进程隔离的 JSON-RPC 插件与 MCP 服务器。仅支持 Linux/macOS，不支持 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- daemon+薄客户端架构：会话可恢复、多终端共享、daemon 热重载
- 命名多 agent 并行调度与 /auto 自主驱动、watcher 舰队监督
- 凭据 broker：短时效作用域 token，agent 不接触长期凭据
- 任意语言进程隔离扩展 + MCP 服务器 + JSON-RPC/WebSocket 嵌入接口

## 适用场景

- 在终端里同时跑多个并行 AI agent 完成编码任务
- 无人值守地运行和监督 agent 舰队（心跳、重启、成本限制）
- 通过 JSON-RPC/WebSocket API 将 agent 引擎嵌入其他软件
- 用本地 Ollama 无凭据起步运行 agent

## 场景标签

`多智能体` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L21: Synaps is an agent runtime written in Rust. It runs agents with built-in tools, subagents, and extensions against a
> L113: |`synaps rpc`|JSON-RPC over stdio. Embed the engine in other software|

## 星数曲线

```mermaid
xychart-beta
    title "HaseebKhalid1507/SynapsCLI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-30 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b77e983fa551` · [字段定义](../../DATASET.md)*
