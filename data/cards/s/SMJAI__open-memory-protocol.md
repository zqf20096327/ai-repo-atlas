# SMJAI/open-memory-protocol

⭐ 86 · TypeScript · NOASSERTION · 推送 2026-07-02 · [GitHub](https://github.com/SMJAI/open-memory-protocol) · 个人维护

**跨工具共享 AI 记忆的开放协议与参考服务器**

供应商中立的规范，定义 AI 工具如何存储、检索与共享用户记忆：包含 Memory Object 模式、记忆类型（episodic/semantic/procedural）、REST API、认证与导入导出。同时提供可用 Docker 一条命令运行的自托管参考服务器、TypeScript/Python SDK 计划，以及面向 Claude（MCP）、OpenAI、Cursor 等工具的适配器。通过 OMP Bridge 浏览器扩展可在 ChatGPT、Claude.ai、Gemini、Perplexity 网页版间保存与交接对话记忆。面向希望打通多个 AI 工具记忆的开发者与用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义 Memory Object/记忆类型/REST API/认证/导入导出的规范
- 自托管参考服务器（npx omp-server 或 Docker 单命令运行）
- Claude（MCP）、Claude Code、Cursor、Copilot、Codex CLI 等适配器
- OMP Bridge 浏览器扩展支持跨网页 AI 工具对话交接

## 适用场景

- 让 Claude 记住的偏好可被 Cursor 或自建 agent 读取
- 在不同 AI 工具间自动延续同一对话上下文
- 自托管服务器集中管理并自主掌控 AI 记忆数据

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L29: **Open Memory Protocol** is a vendor-neutral specification for how AI tools store, retrieve, and share memory about
> L32: - **A specification** — a precise definition of memory objects, storage format, and HTTP API
> L33: - **A reference server** — self-hostable, open-source, runs in Docker in one command

## 星数曲线

```mermaid
xychart-beta
    title "SMJAI/open-memory-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-30 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `eba9eed0433b` · [字段定义](../../DATASET.md)*
