# rergards/mempalace-code

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/rergards/mempalace-code) · [官网](https://pypi.org/project/mempalace-code/) · 个人维护

**本地优先的 AI 编程记忆层：29 个 MCP 工具+时序知识图谱+本地向量检索**

面向开发者的离线优先 AI 记忆工具：把代码库、架构决策、调试会话与对话导出一次性索引到本地向量存储，通过 29 个 MCP 工具供 Claude Code、Codex CLI、Cursor、Windsurf 等 MCP 兼容客户端检索，无云服务与 API key。机制上提供语言感知的 AST/自适应分块挖掘、带时效窗口的时序知识图谱（SQLite 图）、跨项目检索（tunnels）与按 profile（minimal/kg/code/notes/full）裁剪工具面。自称实测峰值节省 33.8x token。限制：Kubernetes Secret 外的凭据文件不被自动检测，需用户用 .gitignore/scan_skip_globs 排除。以 Python 包经 uv/pipx 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 个 MCP 工具，支持 minimal/kg/code/notes/full 五种 profile 裁剪
- 时序知识图谱：事实带有效性窗口，存于独立 SQLite 图
- 本地向量检索与一次性索引，无云服务、无 API key
- 索引 20+ 种语言的代码文件及 Claude Code/Codex/Gemini CLI/ChatGPT/Slack 等对话导出

## 适用场景

- 让编程 agent 跨会话、跨项目回忆架构决策与调试历史
- 把手写记忆文件作为补充，把易变事实迁入时序知识图谱
- 在多个项目间搜索同一主题（如 auth）的历史上下文

## 场景标签

`Agent 记忆` `知识图谱` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18:  29 MCP Tools Any MCP-capable agent search, store, traverse · static profiles
> L123: mempalace-code works with any MCP-compatible client:

## 星数曲线

```mermaid
xychart-beta
    title "rergards/mempalace-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `dc0732b4c245` · [字段定义](../../DATASET.md)*
