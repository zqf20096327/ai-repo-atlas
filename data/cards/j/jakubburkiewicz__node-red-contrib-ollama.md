# jakubburkiewicz/node-red-contrib-ollama

⭐ 30 · HTML · MIT · 推送 2026-10-28 · [GitHub](https://github.com/jakubburkiewicz/node-red-contrib-ollama) · [官网](https://jakubburkiewicz.github.io/node-red-contrib-ollama/) · 个人维护

**把 Ollama 封装为 Node-RED 节点的集成模块**

封装 ollama.js 库的 Node-RED 模块，将 Ollama 的能力以可配置节点形式接入流程，覆盖 Chat、Generate、Embed、模型创建/复制/删除/拉取/推送、列出模型、中止流式生成等操作。支持连接本地 Ollama 服务（默认端口 11434）或 Ollama Cloud（API key，端口 443）。要求 Node.js 18+ 与已安装的 Node-RED，通过编辑器管理面板或 npm 安装。

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

- 提供 Chat/Generate/Embed 等 12 个 Ollama 操作节点
- 支持本地 Ollama 服务与 Ollama Cloud 两种连接方式
- 通过 Node-RED 编辑器或 npm 命令行安装

## 适用场景

- 在 Node-RED 流程中直接调用 Ollama 生成对话或回答
- 在流程里执行模型拉取、删除、嵌入生成等管理操作
- 无手写代码把 Ollama 接入现有自动化流程

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: A Node-RED module that wraps the ollama.js library, offering its functionalities as configurable nodes for easy inte
> L70: - **Chat**: Generate the next message in a chat with a provided model.

## 星数曲线

```mermaid
xychart-beta
    title "jakubburkiewicz/node-red-contrib-ollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9411fc23647e` · [字段定义](../../DATASET.md)*
