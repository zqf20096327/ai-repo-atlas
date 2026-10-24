# wiseaidotdev/autogpt

⭐ 116 · Rust · MIT · 推送 2026-06-20 · [GitHub](https://github.com/wiseaidotdev/autogpt) · [官网](https://autogpt.wiseai.dev) · 个人维护

**纯 Rust 的 AI agent 构建框架，含 9 个内置 agent 与编排模式**

AutoGPT 是一个用 Rust 编写的 AI agent 创建与管理框架，面向希望以声明式 YAML 定义 agent 的开发者。提供工具与传感器、向量长期记忆、规划器、MCP 协议支持、多后端 Mixture of Providers 并行打分等机制；内置 9 个专门化 agent（ArchitectGPT、BackendGPT 等）。支持 4 种运行模式：交互式 TUI、直接 prompt、独立 agent、经 TLS+Protobuf TCP 由 orchgpt 编排的分布式模式。README 标注 Work In Progress、建议 Linux 环境，通过 cargo 可执行文件或 Docker 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YAML 声明式配置 agent，无需编码
- MCP 协议一等支持（Stdio/SSE/HTTP）连接外部工具服务器
- Mixture of Providers 跨多 AI 后端并行扇出并加权评分
- IAC 协议支持 agent 间 TLS+Protobuf 加密通信与编排

## 适用场景

- 用 CLI 直接向 LLM 提问或混合多后端取最优回答
- 以多 agent 协作方式生成全栈应用的前后端代码
- 通过 YAML 定义并运行自定义自动化 agent

## 场景标签

 · 领域:AI agent 框架/LLM 基础设施

## 证据(README 行号)

> L38: AutoGPT is a pure rust framework that simplifies AI agent creation and management for various tasks. Its remarkable
> L52: - 🔌 **MCP (Model Context Protocol)**: First-class support to seamlessly connect external tool servers (Stdio, SSE, 

## 星数曲线

```mermaid
xychart-beta
    title "wiseaidotdev/autogpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-24 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5078fb427e5c` · [字段定义](../../DATASET.md)*
