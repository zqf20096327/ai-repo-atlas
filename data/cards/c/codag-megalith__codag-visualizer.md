# codag-megalith/codag-visualizer

⭐ 671 · TypeScript · MIT · 推送 2026-02-11 · [GitHub](https://github.com/codag-megalith/codag-visualizer) · [官网](https://codag.ai/) · 个人维护

**在 VSCode 中可视化代码库中 AI/LLM 工作流的扩展**

Codag 是一个 VSCode 扩展加本地后端的工具：用 tree-sitter 解析 Python、TypeScript、Go、Rust 等 10+ 语言的代码，通过模式匹配检测 LLM API 调用与 AI 框架用法，再由 Gemini 2.5 Flash 后端识别工作流语义，生成交互式 DAG 图；节点可点击跳转源码，编辑文件后图实时增量更新，并可导出 PNG。面向维护 LLM 相关代码的 AI 工程师与 agent 开发者。需配置 Gemini API key（免费层可用），支持 Docker 或 make 运行后端；扩展另自动注册 MCP Server 供 Cursor Agent、Claude Code 等编码 agent 访问工作流图。

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

- tree-sitter 解析 10+ 语言，自动检测 LLM 调用与决策分支
- 交互式 DAG 图，节点点击跳转到源码行号
- 文件编辑后实时增量更新（AST diff，无需 LLM 往返）
- 内置 MCP Server 供 Cursor Agent / Claude Code 等编码 agent 使用

## 适用场景

- 调试多文件、多 LLM 调用的 agent 链路，定位某次修改影响的分支
- 接手他人的 LangChain / 多 agent 项目时快速理解代码结构
- 导出工作流图用于文档与评审

## 场景标签

 · 领域:开发者工具/代码可视化

## 证据(README 行号)

> L12: Codag analyzes your code for LLM API calls and AI frameworks, then generates interactive workflow graphs — directly
> L41: **Built for** AI engineers, agent builders, and anyone maintaining code that talks to LLMs — whether it's a single 

## 星数曲线

```mermaid
xychart-beta
    title "codag-megalith/codag-visualizer 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24", "2026-10-26"]
    y-axis "stars" 667 --> 672
    line [668, 669, 670, 671, 671]
```

2026-10-18 668 → 2026-10-26 671（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e3d41c58a814` · [字段定义](../../DATASET.md)*
