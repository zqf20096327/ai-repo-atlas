# JoeCastrom/mcp-chat-studio

⭐ 18 · JavaScript · MIT · 推送 2026-04-28 · [GitHub](https://github.com/JoeCastrom/mcp-chat-studio) · 个人维护

**面向 MCP Server 开发者的本地测试调试平台**

基于 Node.js 的 Model Context Protocol 服务器测试工具：提供 Classic 侧边栏与 Workspace 无限画布两种布局，支持工作流断点调试、场景录制回放、批量测试与延迟热力图、契约测试与 Schema 漂移监控、响应 Diff、Mock 服务器与可视化 MCP 服务器生成器（含 OpenAPI 导入）、文档生成与 CI 门禁导出。接入 Ollama 可零配置无 API key 启动，共支持 9 家 LLM 提供商切换。提供 Docker 支持与安全加固，定位为本地开发测试台，不面向公网暴露。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作流断点调试与单步执行、变量检查
- 场景录制回放、批量测试、跨服务器 Matrix 对比与响应 Diff
- 契约测试（14 种断言操作符）+ Schema 漂移检测 + CI 门禁
- 可视化 MCP 服务器生成器，支持 OpenAPI 导入与 Python/Node 代码生成
- 9 家 LLM 提供商 + 自定义，Ollama 零配置免 API key

## 适用场景

- 开发 MCP 服务器时自动化测试全部工具而无需手动点击
- 在 GPT-4、Claude、Llama 等模型间对同一任务做对比
- 团队共享测试场景与环境配置，接入 CI 检测 Schema 漂移
- 从 OpenAPI 规格快速生成并调试 MCP 服务器

## 场景标签

`代码生成` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L5: Test, debug, and develop Model Context Protocol servers with a beautiful glassmorphism UI and a powerful Workspace m
> L203: - **🔧 9 LLM Providers + Custom** - Ollama, OpenAI, Claude, Gemini, Azure, Groq, Together AI, OpenRouter + Custom

## 星数曲线

```mermaid
xychart-beta
    title "JoeCastrom/mcp-chat-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b36fe41ebc79` · [字段定义](../../DATASET.md)*
