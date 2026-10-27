# pguso/mcp-from-scratch

⭐ 36 · JavaScript · MIT · 推送 2026-05-25 · [GitHub](https://github.com/pguso/mcp-from-scratch) · 个人维护

**零依赖 Node.js 从零实现 MCP 服务器的分步教程**

面向初学者的学习仓库：用纯 Node.js 从零构建一个可连接 Claude Desktop 的 MCP 服务器，从 JSON-RPC 与 stdio 传输讲到 tools、prompts、resources、sampling 与 agent 工作流。模块 01–10 及模块 11 服务端不使用任何 npm 依赖，每模块以 README+注释源码+run.md 三段组织，并链接 MCP 规范（2025-11-25）对应章节。例外是模块 11/12 的客户端通过 node-llama-cpp 运行本地 GGUF 模型（默认 Qwen，约 1.5-1.6 GB），模块 12 含可选 LangChain 示例。明确声明不是生产级 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分模块从零实现 MCP 协议，模块 01–10 零 npm 依赖
- 构建的 MCP 服务器可直接连接 Claude Desktop 或任意 MCP 客户端
- 模块 11/12 客户端用 node-llama-cpp 运行本地 GGUF 模型
- 每个模块链接 MCP 规范 2025-11-25 对应章节

## 适用场景

- 想理解 MCP SDK 底层原理的开发者按模块自学
- 动手实现一个无黑盒的 MCP 服务器并接入桌面客户端
- 学习 MCP 与本地模型、agent 工作流的结合方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A learning repository for complete beginners. No frameworks. No black boxes. Pure Node.js.
> L5: By the end you will have built a working MCP server you can connect to Claude Desktop - and you will understand ever
> L82: It is not a production MCP SDK. It is not the fastest path to shipping. It is not a collection of examples you copy

## 星数曲线

```mermaid
xychart-beta
    title "pguso/mcp-from-scratch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-27 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `58f54bc70eb3` · [字段定义](../../DATASET.md)*
