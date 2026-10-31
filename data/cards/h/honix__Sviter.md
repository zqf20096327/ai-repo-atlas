# honix/Sviter

⭐ 14 · TypeScript · NOASSERTION · 推送 2026-06-25 · [GitHub](https://github.com/honix/Sviter) · 个人维护

**内置自主 AI Agent 的协作文档知识库（自托管 wiki）**

基于 Git 与 Markdown 文件的自托管 wiki：数据为纯 Markdown 存于用户 git 仓库，无数据库；提供 AI 问答、自主 Agent 在分支上修改内容并由用户审阅 diff 后合并或丢弃、提示词生成自定义交互视图、实时协作与鉴权同步。LLM 后端可插拔：Claude Agent SDK 或 OpenRouter，支持 BYOK 或本地推理服务。通过 make 命令从源码安装运行前后端。README 自称 MVP 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自主 Agent 在 git 分支上改文档，用户审阅 diff 后合并/丢弃
- 数据为用户 git 仓库中的纯 Markdown，无数据库锁定
- LLM 可插拔：Claude Agent SDK 或 OpenRouter（BYOK/本地推理）
- 提示词生成按需交互式自定义视图

## 适用场景

- 团队知识库：开发者提问、写作者更新文档，git 细节隐藏
- 规格驱动开发：在 wiki 写规格，AI 保持文档与代码同步
- 研究笔记：AI 帮助跨页面交叉引用与连接想法

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AI-powered wiki where autonomous agents help you build and maintain knowledge.
> L11: - **AI Chat** — Ask questions about your wiki, history, and active threads
> L12: - **Autonomous Agents** — Request changes, AI works on a branch, you review and accept/reject
> L16: - **Pluggable LLM** — Claude Agent SDK or OpenRouter — BYOK or connect to your local inference services

## 星数曲线

```mermaid
xychart-beta
    title "honix/Sviter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2852a6884a5b` · [字段定义](../../DATASET.md)*
