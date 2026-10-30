# hieuchaydi/RepoBrain

⭐ 27 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/hieuchaydi/RepoBrain) · [官网](https://docs-repobrain-orpin.vercel.app/) · 个人维护

**给 AI 编码代理的本地代码库索引与预合并安全门工具**

Python 编写的源码仓库索引与查询工具：对代码库建立本地索引（写入 .repobrain/，含向量和元数据），提供混合检索（词法+本地向量+重排）、流程追踪、影响分析与编辑目标排序。定位为 AI 编码代理的预合并安全层，提供 CLI、stdio MCP 服务器（可嵌入 Claude Code/Cursor/Codex）与本地浏览器 UI 三种接口，含 blast 影响评分、ship 门禁、patch 审查与 SAFE/WARN/BLOCK 安全裁决。默认本地运行，Gemini/OpenAI/Voyage/Cohere/Groq 为可选远程 provider，需显式配置。支持 pip 安装、Docker 及 Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 词法+本地向量混合检索并重排，返回带评分的文件与片段
- stdio MCP 集成，提供 search/trace/impact/blast/ship/gate 等 20+ 工具
- 本地浏览器 UI（React 前端）与 CLI 双入口
- 默认本地运行，远程 provider 需显式 opt-in 配置

## 适用场景

- 在 Claude Code/Cursor 等编辑器代理中做代码检索与影响分析
- 代理改代码前评估 blast radius 风险并做预合并门禁检查
- 本地索引并查询跨仓库代码，记录仓库记忆笔记

## 场景标签

`语义搜索` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: RepoBrain is a Python tool that indexes source repositories and serves query results through a consistent local inte
> L14: - `repobrain serve-mcp` for stdio MCP integration with editor agents
> L38: This is what makes RepoBrain different — it runs inside Claude Code, Cursor, and Codex as a live tool, not as a sep

## 星数曲线

```mermaid
xychart-beta
    title "hieuchaydi/RepoBrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `e7adda6094d8` · [字段定义](../../DATASET.md)*
