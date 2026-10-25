# Goldziher/basemind

⭐ 113 · Rust · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Goldziher/basemind) · [官网](https://basemind.ai) · 个人维护

**给编码 agent 的 MCP 上下文与通信层服务器**

用 Rust 实现的单一 MCP 服务器，为编码 agent 提供代码库的持久上下文：基于 tree-sitter 的代码地图（300+ 语言的 outline/symbols/definition/references 等）、代码图遍历与导出、git 历史与 blame 查询、按仓库隔离的共享记忆与 90+ 格式文档语义检索、网页抓取、agent 间线程通信与后台 shell 会话，并输出节省 token 的统计。安装途径包括插件方式（支持 Claude Code、Codex、Cursor、Gemini CLI 等 10+ agent 宿主）、MCP 服务器配置与 crates.io/PyPI/npm 程序安装。限制：语义代码搜索需 --features code-search，PyPI 0.29.3 早于技能注册修复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 MCP 服务器同时提供代码地图、代码图、git 情报、共享记忆、文档 RAG、网页抓取与 agent 通信
- 300+ 语言代码情报与 90+ 文档格式语义检索（PDF/Office/HTML/邮件/图片 OCR）
- 10+ agent 宿主的插件安装路径（Claude Code、Codex、Cursor、Gemini CLI、Copilot 等）
- 代码图可视化导出（DOT/Mermaid/GraphML/交互式 HTML）与 token 节省遥测

## 适用场景

- 让编码 agent 以文件路径+行号+签名回答代码问题而非读整个文件
- 多 agent 团队通过共享线程协调对同一仓库的工作
- 跨 PDF/Office/网页资料的语义检索供 agent 引用
- 查询函数级 git 变更历史与 blame

## 场景标签

`多智能体` `网页抓取` `RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **The context and communication layer for coding agents.**
> L196: ### 2. As an MCP server
> L198: If your tool speaks MCP but you're not using the plugin, install the program,

## 星数曲线

```mermaid
xychart-beta
    title "Goldziher/basemind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-25 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `af821f6ad231` · [字段定义](../../DATASET.md)*
