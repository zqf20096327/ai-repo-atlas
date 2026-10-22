# zamalali/DeepGit

⭐ 922 · Python · MIT · 推送 2026-08-30 · [GitHub](https://github.com/zamalali/DeepGit) · [官网](https://deepgit.vercel.app) · 个人维护

**帮开发者用自然语言找最匹配 GitHub 仓库的 agentic 研究引擎**

DeepGit 是面向 GitHub 的 agentic 搜索引擎：将自然语言请求解析为搜索角度、硬约束与反模式，经 GitHub GraphQL 批量检索、本地向量索引语义召回（LanceDB + fastembed，可选）、零成本预筛与证据评分，对不确定的候选会读取真实源码后重判。典型查询约 2 次 LLM 调用。可作 Python 库、CLI 使用，并内置 MCP 服务器供 Claude Desktop、Cursor、VS Code 等客户端调用。需配置 GitHub token 与 LLM 提供商（groq/openai/anthropic/vertex_ai）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 意图保持的 agentic 检索管线：关键词+主题+语义多角度搜索
- 不确定性驱动的升级机制，不确定时读取真实源码与测试重判
- 内置 MCP 服务器，暴露 4 个工具（find_repositories/deep_research 等）
- 本地向量索引语义召回随使用积累（LanceDB + fastembed）

## 适用场景

- 用一句自然语言找最符合需求的 GitHub 仓库
- 在 Claude Desktop/Cursor 等 MCP 客户端里让助手调用仓库研究能力
- 高风险技术选型时让 agent 读源码做对比报告

## 场景标签

 · 领域:开发者工具/AI 搜索

## 证据(README 行号)

> L11: **DeepGit** is an agentic research engine for GitHub. Instead of collapsing your
> L65: 1. **Understand the intent.** One LLM call turns your request into a plan: search angles, GitHub topics, hard *must
> L173: |`find_repositories(intent, limit=5)`|Ranked Markdown report|Everyday "find me the best repo for X". Fast, reads c

## 星数曲线

```mermaid
xychart-beta
    title "zamalali/DeepGit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 921 --> 923
    line [922, 922]
```

2026-10-18 922 → 2026-10-22 922（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c51f13f8d996` · [字段定义](../../DATASET.md)*
