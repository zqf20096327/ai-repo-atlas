# JK-Ai-Era/octopi

⭐ 97 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/JK-Ai-Era/octopi) · 个人维护 · 中文 README

**可嵌入的 Agent 引擎：为产品提供会话运行时与治理**

Octopi 定位为可嵌入的 agent 引擎：宿主产品保留身份与权限边界（Principal/Intent/IAM），引擎提供会话持久化、记忆基底（Memory/Cognition/Wisdom 存于 SQLite）、上下文管线、工具治理与监督运行。Agent 以目录形式定义（Markdown 人设与技能），CLI 提供初始化向导、TUI 聊天与网关服务，Web 控制台支持浏览器配置。要求 Node.js ≥ 24，以 npm 包分发，支持 personal/organization/multi-organization 部署模式。

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

- 会话连续性与记忆基底作为一等对象，SQLite 存储
- 宪法式本体与不变量（I1-I6）约束引擎实现
- 工具来源支持内置、宿主注册与 MCP 服务器，命名空间防冲突
- CLI/Web 双向导与非交互式 --yes 模式适配 CI/脚本安装

## 适用场景

- 在自己的产品中嵌入带持久会话与记忆的 agent 运行时
- 搭建需要多组织隔离与访问密钥的 agent 部署
- 通过 MCP 与自定义工具扩展 agent 能力边界

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L34: Octopi is an **embeddable agent engine** — a component you build AI-powered
> L40: - **The engine keeps the runtime.** Session, Run, memory, context, tools,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cf368e926521` · [字段定义](../../DATASET.md)*
